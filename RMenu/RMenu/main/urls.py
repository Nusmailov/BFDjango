from django.urls import path
from main import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('restaurants/', views.res_list, name='restaurants'),
    path('dishes/', views.dish_list, name='dishes'),
    path('dishes/new', views.res_new, name='resnew')
]
