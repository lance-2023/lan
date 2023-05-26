import json

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.serializers import CustomerSerilizer
from customer.models import Customer
from rest_framework.response import Response
from rest_framework import status
import requests


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer

    def create(self, request, *args, **kwargs):
        data = request.data
        #data是dict类型，需要转换格式
        print(data)

        url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/customers'
        headers = {'x-auth-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}

        #这里只用json参数，转换data类型，在bc端接受的是json数据，而不是data参数
        resp = requests.post(url=url, json=data, headers=headers)
        print(resp.text)
        print("\n")
        print(resp.status_code)
        #在bc端创建成功后才会在，我们这边创建
        if resp.status_code == 201:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)

        # 报错上面代码已经用过request.data调用父类方法中有request.data此时已经没有数据，只能调用一次
        # super().create(self, request, *args, **kwargs)



        return Response(data={
            'detail': resp.text,
            'data': data
        }, headers=headers, status=resp.status_code)
