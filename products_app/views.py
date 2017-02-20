from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from products_app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'products_app/list_products.html'

class CreateProductSuccess(TemplateView):
    template_name = 'products_app/create_product_success.html'

def list_products(request):
    return render(request, 'products_app/list_products.html', {
        'products_list': models.Product.objects.all()
        })

def create_a_product(request):
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
