from audioop import reverse
from contextlib import redirect_stderr
from django.utils import timezone
from django.shortcuts import render, redirect
from order.models import Shop, Menu, Order, Orderfood
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.serializers import ShopSerializer, MenuSerializer

# Create your views here.

@csrf_exempt
def shop(request):
    if request.method=='GET':
        # shop=Shop.objects.all()
        # serializer=ShopSerializer(shop, many=True)
        # return JsonResponse(serializer.data, safe=False)
        
        shop=Shop.objects.all()
        return render(request, 'order/shoplist.html', {'shop_list':shop})
        
        
    elif  request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt        
def menu(request, shop_id ):
    if request.method=='GET':
        # menu=Menu.objects.all()
        # serializer=MenuSerializer(menu, many=True)
        # return JsonResponse(serializer.data, safe=False)
        menu=Menu.objects.filter(shop=shop_id)
        return render(request, 'order/menulist.html', {'menu_list':menu, 'shop_id': shop_id})
        
    elif  request.method=='POST':
        data=JSONParser().parse(request)
        serializer=MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400)        

@csrf_exempt        
def order(request):
    if request.method=='POST':
        shop_id=request.POST['shop_id']
        address=request.POST['address']
        order_date=timezone.now()
        food_list=request.POST.getlist('menu')
        
        order_item=Order(shop=Shop.objects.get(pk=shop_id), address=address, order_date=order_date)
        order_item.save() 

        
        for food in food_list:
            food_item=Orderfood(order=Order.objects.latest('id'), food_name=food )
            food_item.save()
        
        return render(request, 'order/success.html')
    
    elif request.method=='GET':
        order=Order.objects.all()
        return render(request, 'order/orderlist.html', {'order_list':order})

 