from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from order.serializers import OrderSerializer
from order.models import Order
from rest_framework.exceptions import ValidationError
import requests

from utils.api_response import APIResponse
from rest_framework import status


# Create your views here.

# class OrderReadOnlyViewSet(ReadOnlyModelViewSet) 只能读取数据

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/orders'
        headers = {'x-auth.py-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}
        requests.post(url=url, json=data, headers=headers)

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, message="数据校验出错", data=data)
        return APIResponse(code=status.HTTP_201_CREATED, message="创建成功", data=data)

    # 报错上面代码已经用过request.data调用父类方法中有request.data此时已经没有数据，只能调用一次
    # super().create(self, request, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #
    #     # BC API对接
    #     # url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/orders'
    #     # headers = {'x-auth.py-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}
    #     #
    #     # # 这里只用json参数，转换data类型，在bc端接受的是json数据，而不是data参数
    #     # BC_response = requests.post(url=url, json=data, headers=headers)
    #     # BC_data = BC_response.json()
    #     # # print(BC_response.text)
    #     # # print("\n")
    #     # # print(BC_response.status_code)
    #     serializer = self.get_serializer(data=request.data)
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #     except ValidationError:
    #         return APIResponse(code=status.HTTP_400_BAD_REQUEST, message="数据校验出错", data=data)
    #     return APIResponse(code=status.HTTP_201_CREATED, message="创建成功", data=data)

