'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers
from  order.models import Order
#模型序列化器
class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        #设置你需要的字段
        # fields = []
        fields = '__all__'
        #除了某字段不要，其他都要
        # ecclude = []
