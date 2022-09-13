from django.urls import path
from user import views


app_name='user'
urlpatterns = [
    path('user/' , views.user , name='user'),
    path('login/' , views.login , name='login')
]
