from audioop import reverse
from contextlib import redirect_stderr
from django.utils import timezone
from django.shortcuts import render, redirect
from order.models import Shop, Menu, Order, Orderfood
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.serializers import ShopSerializer, MenuSerializer

@csrf_exempt
def order_list(request, shop_id):
    if request.method=='GET':
        order=Order.objects.filter(shop=shop_id)
        return render(request, 'boss/orderlist.html', {'order_list':order})
    else:
        return HttpResponse(status=404)
    
@csrf_exempt
def timeinput (request):
    if request.method=='POST':
        order_item=Order.objects.get(pk=request.POST['orderid'])
        shop_id=order_item.shop.id
        order_item.estimate_time=request.POST['estimated_time']
        order_item.save()
        return render(request, 'boss/success.html', {'shop_id': shop_id})
    else:
        return HttpResponse(status=404)