from django.urls import path
from main import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('base/', views.base, name='base'),
    path('shops/', views.shop_list, name='shops'),
    path('shop/<int:pk>', views.shop_detail),
    path('cities/', views.city_list, name='cities'),
    path('city/<int:pk>/', views.city_detail),
    path('flowers/', views.flower_list, name='flower'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # path('loginjwt/', obtain_jwt_token, name='loginjwt'),
    # path('registerjwt/', views.registerr, name='registerjwt'),
    path('loginn/', views.loginn, name="loginn"),
    path('registerr/', views.registerr, name="registerr"),
]
