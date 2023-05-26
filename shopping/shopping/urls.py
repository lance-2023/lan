"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from customer.views import CustomerViewSet
from product.views import ProductViewSet
from django.urls import include

customer_router = DefaultRouter()
customer_router.register('customer', CustomerViewSet)

product_router = DefaultRouter()
product_router.register('product', ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
#基于视图集，包：include以及实现的router
    path('api/v1/', include(customer_router.urls)),
    path('api/v1/', include(product_router.urls))
]
