from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from products_app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'products_app/login.html'

class Register(TemplateView):
    template_name = 'products_app/register.html'

def list_products(request):
    if not request.user.is_authenticated:
        return render(request, 'products_app/login.html', {'page_info': 'You must login to view products.'})

    return render(request, 'products_app/list_products.html', {
        'products_list': models.Product.objects.all()
        })

def create_a_product(request):
    if not request.user.is_authenticated:
        return render(request, 'products_app/login.html', {'page_info': 'You must login to create products.'})

    data = request.POST
    p = models.Product(
        name=data['product_name'],
        category=data['product_category'],
        price=data['product_price']
    )
    
    p.save()
    
    return render(request, 'products_app/create_product_success.html', {
        'product': p
        })

def register_user(request):
    data = request.POST
    User.objects.create_user(
        username=data['username'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        password=data['password']
    )
    return login_user(request)


def login_user(request):
    data = request.POST
    username = data['username']
    password = data['password']
    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        login(request=request, user=user)
    else:
        return render(request, 'products_app/login.html', {'page_info': 'User Email and Password Match not Found.'})
    return HttpResponseRedirect(redirect_to='/home')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(redirect_to='/')
