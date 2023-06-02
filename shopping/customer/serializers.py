"""
author:lance.lan
date:2023/5/24
project:djangoProject
"""
from rest_framework import serializers
from customer.models import Customer, Authentication


# 模型序列化器
class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ['password', 'password_confirmation', 'force_reset']


class CustomerCreateSerializer(serializers.ModelSerializer):
    # 序列化外键法一：
    authentication = AuthenticationSerializer()
    # 法二：
    # authentication = serializers.SerializerMethodField()
    # def get_authentication(self, obj):
    #     authentication = obj.authentication
    #     authentication_list = []
    #     if authentication.password:
    #         authentication_list.append({'password': authentication.password})
    #     if authentication.password_confirmation:
    #         authentication_list.append({'password_confirmation': authentication.password_confirmation})
    #     if authentication.force_reset:
    #         authentication_list.append({'force_reset': authentication.force_reset})
    #     return authentication_list

    class Meta:
        model = Customer
        # 设置你需要的字段
        # fields = []
        fields = '__all__'
        # 除了某字段不要，其他都要
        # exclude = []



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # 设置你需要的字段
        # fields = []
        # fields = '__all__'
        # 除了某字段不要，其他都要
        exclude = ['authentication']
