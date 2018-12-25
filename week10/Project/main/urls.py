from django.urls import path
from main import views

urlpatterns = [
    path('', views.base, name='home'),
    path('author/', views.author_list, name='author'),
    path('book/', views.book_list, name='book'),
    path('author/new/', views.author_new, name='author_new'),
    path('delete_author/<int:author_id>', views.delete_author, name="delete_author"),
    path('update_author/<int:author_id', views.update_author, name='update_author'),
]