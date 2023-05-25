from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.serializers import CustomerSerilizer
from customer.models import Customer
# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer

    # @action