'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers
from  product.models import Product
#模型序列化器
class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #设置你需要的字段
        # fields = []
        fields = '__all__'
        #除了某字段不要，其他都要
        # ecclude = []
