from django.urls import path
from . import views


urlpatterns = [
    path('rest_list/', views.rest_list),
    path('rest_detail/<int:pk>',views.RestaurantDetail.as_view()),
    path('login/',views.login)
]