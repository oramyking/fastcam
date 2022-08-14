from django.contrib import admin
from django.urls import path, include
from delivery import views

app_name='delivery'
urlpatterns = [
    path('delivery/'             ,  views.delivery_list       , name='delivery_list')
]
