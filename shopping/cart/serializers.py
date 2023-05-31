'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers
from  cart.models import Cart
#模型序列化器
class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        #设置你需要的字段
        # fields = []
        fields = '__all__'
