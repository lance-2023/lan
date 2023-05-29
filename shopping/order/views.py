from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.serializers import OrderSerilizer
from order.models import Order
from rest_framework.response import Response
from rest_framework import status
import requests
# Create your views here.

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizer