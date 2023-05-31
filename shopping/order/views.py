from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from order.serializers import OrderSerilizer
from order.models import Order
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import requests

from utils.api_response import APIResponse


# Create your views here.

# class OrderReadOnlyViewSet(ReadOnlyModelViewSet) 只能读取数据

class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerilizer

    # 报错上面代码已经用过request.data调用父类方法中有request.data此时已经没有数据，只能调用一次
    # super().create(self, request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        data = request.data
        # data是dict类型，需要转换格式
        print(data)

        url = 'https://api.bigcommerce.com/stores/rmz2xgu42d/v2/orders'
        headers = {'x-auth-token': 'ol999cchp7xq536507sq3pbjia3fi43', 'Accept': 'application/json'}

        # 这里只用json参数，转换data类型，在bc端接受的是json数据，而不是data参数
        BC_response = requests.post(url=url, json=data, headers=headers)
        BC_data = BC_response.json()
        # print(BC_response.text)
        # print("\n")
        # print(BC_response.status_code)
        if BC_response.status_code == 201:
            serializer = self.get_serializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except ValidationError:
                return APIResponse(code=ValidationError.status_code, message="数据校验出错", data=data)
            return APIResponse(code=BC_response.status_code, message="创建成功", data=BC_data)
        else:
            return APIResponse(code=BC_response.status_code, message=BC_data[0]["message"], data=data)
