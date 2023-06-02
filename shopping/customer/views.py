import time

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.serializers import CustomerSerializer, CustomerCreateSerializer
from customer.models import Customer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
import requests
from utils.api_response import APIResponse
import jwt
from django.conf import settings
from rest_framework import status


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # 报错如果代码已经用过request.data调用父类方法中有request.data此时已经没有数据，只能调用一次
    # super().create(self, request, *args, **kwargs
    def create(self, request, *args, **kwargs):
        data = request.data
        # data是dict类型，需要转换格式
        print(data)

        url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/customers'
        headers = {'x-auth-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}
        requests.post(url=url, json=data, headers=headers)

        # 这里只用json参数，转换data类型，在bc端接受的是json数据，而不是data参数
        # BC_response = requests.post(url=url, json=data, headers=headers)
        # BC_data = BC_response.json()
        # print(resp.text)
        # print(type(resp.text))
        # print("\n")
        # print(resp.json())
        # print(type(resp.json()))
        # print("\n")
        # print(BC_response.status_code)
        # 在bc端创建成功后才会在，我这边创建
        # if BC_response.status_code == 201:
        # else:
        # return APIResponse(code=BC_response.status_code, message=BC_data[0]["message"], data=data)

        serializer = CustomerCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, message="数据校验出错", data=data)
        return APIResponse(code=status.HTTP_201_CREATED, message="创建成功", data=data)


    @action(methods=['GET'], detail=False)
    def login(self, request):
        login_data = request.data
        customer = self.get_queryset().filter(
            email=login_data['email']
        ).first()
        print(customer.authentication.password)
        print(login_data['password'])
        # 这里用filter进行查询操作，filter返回的是满足条件的对象列表，如果知道只有一个，则加上first来返回该对象
        if not customer:
            return APIResponse(code=404, message='用户不存在', data=login_data)
        if customer.authentication.password == login_data['password']:
            return APIResponse(code=400, message='密码不正确', data=login_data)
        payload = {
            'email': customer.email,
            'exp': int(time.time()) + 60
        }
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY)
        return APIResponse(code=200, message='密码正确', data=token)
