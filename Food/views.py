from django.shortcuts import render
from . models import Pizaa,Burger
# Create your views here.
def index(request):
    ctx = {'active_link':'index'}
    return render(request,'Food/index.html',ctx)

def pizza(request):
    pizzas = Pizaa.objects.all()
    ctx = {'pizza' : pizzas,'active_link':'pizza'}
    return render(request,'Food/pizza.html',ctx)

def burger(request):
    burger = Burger.objects.all()
    ctx = {'burger': burger,'active_link':'burger'}
    return render(request,'Food/burger.html',ctx)