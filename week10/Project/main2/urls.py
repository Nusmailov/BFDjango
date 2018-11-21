from django.urls import path
from main2 import views

app_name = 'main2'

urlpatterns = [
    path('students/', views.StudentListView.as_view(template_name="student/student_list.html"), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete')
]

