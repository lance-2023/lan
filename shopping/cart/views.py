from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from cart.serializers import CartSerilizer


# Create your views here.
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerilizer
