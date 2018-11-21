from django.urls import path
from api1 import views


urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
    path('teachers/', views.teacher_list),
    path('teachers/<int:pk>', views.teacher_detail),

]


