from django.shortcuts import render, redirect
from main.models import Review,Restaurant,RestaurantReview,Dish,DishReview
from django.contrib.auth.decorators import login_required
from main.forms import UserForm

# Create your views here.

def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


@login_required
def res_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants':restaurants}
    return render(request, 'restaurants.html', context)


@login_required
def dish_list(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'dish.html', context)


@login_required
def res_new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('restaurants')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request,'new.html', context)

