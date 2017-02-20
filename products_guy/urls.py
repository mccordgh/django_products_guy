"""products_guy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from products_app import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^home/', views.list_products, name='list_products'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logout/', views.logout_user, name= 'logout'),
    url(r'^create_a_product/', views.create_a_product, name='create_a_product'),
]
