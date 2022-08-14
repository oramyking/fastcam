from django.contrib import admin
from django.urls import path, include
from boss import views

app_name='boss'
urlpatterns = [
    path('orders/<int:shop_id>'    , views.order_list, name='order_list'),
    path('timeinput/'              , views.timeinput , name='timeinput'),
]
