from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerilizer
from product.models import Product
from rest_framework.response import Response
from rest_framework import status
import requests
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer