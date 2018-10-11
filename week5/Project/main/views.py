from django.shortcuts import render, redirect
from main.models import Book,Author
from main.forms import AuthorForm
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book.html', context)

def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author.html', context)

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request, 'home.html')


def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'author/new.html', context)

def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    tasks = Author.objects.all()
    context = {
        'tasks': tasks
    }
    return redirect('author')

# Create your views here.
