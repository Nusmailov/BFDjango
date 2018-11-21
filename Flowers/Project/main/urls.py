from django.urls import path
from main import views

urlpatterns = [
    path('shops/', views.shop_list, name='shops'),
    path('shop/<int:pk>', views.shop_detail),
    path('cities/', views.city_list,),
    path('city/<int:pk>/', views.city_detail),
]
