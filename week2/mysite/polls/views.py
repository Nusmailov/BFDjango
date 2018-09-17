from django.shortcuts import render
import django.http


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
