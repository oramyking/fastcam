from django.contrib import admin
from django.urls import path, include
from order import views

app_name='order'
urlpatterns = [
    path('shops/'                , views.shop       , name='shop'),
    path('menus/<int:shop_id>'   , views.menu       , name='menu'),
    path('orders/'               , views.order      , name='order')
]
