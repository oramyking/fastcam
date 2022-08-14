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
def delivery_list(request):
    if request.method=='GET':
        delivery=Order.objects.all()
        return render(request, 'delivery/deliverylist.html', {'delivery_list':delivery})
    
    elif request.method=='POST':
        order_item=Order.objects.get(pk=request.POST['orderid']) 
        order_item.deliver_finish=1
        order_item.save()
        return render(request, 'delivery/success.html')
