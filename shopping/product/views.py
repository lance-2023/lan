from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerializer
from product.models import Product
import requests

from utils.api_response import APIResponse


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def create(self, request, *args, **kwargs):
        data = request.data

        url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v3/catalog/products'
        headers = {'x-auth.py-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}
        requests.post(url=url, json=data, headers=headers)

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, message="数据校验出错", data=data)
        return APIResponse(code=status.HTTP_201_CREATED, message="创建成功", data=data)
