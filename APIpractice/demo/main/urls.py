from django.urls import path
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login/', views.login),
    path('students/', views.GenericTaskList.as_view()),
    path('tasks/', views.TaskList.as_view()),

   # path('students/<int:pk>', views.GenericTaskDetail.as_view() )
]

urlpatterns = format_suffix_patterns(urlpatterns)