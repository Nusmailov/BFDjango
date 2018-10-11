from django.urls import path
from main import views

urlpatterns = [
    path('',views.base, name='base'),
    path('author/', views.author_list, name='author'),
    path('book/', views.book_list, name='book'),
    path('home/', views.home, name='home'),
    path('author/new/', views.author_new, name='author_new'),
    path('delete_author/<int:author_id>', views.delete_author, name="delete_author"),
]
