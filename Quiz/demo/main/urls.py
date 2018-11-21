from django.urls import path
from main import views

urlpatterns = [
    path('adverts/', views.AdvertList.as_view()),
    path('adverts/<int:pk>/', views.AdvertDetail.as_view()),
    path('advertsfb/', views.advert_list),
    path('advertsfb/<int:pk>/', views.advert_detail),
    path('login/', views.login),
]



