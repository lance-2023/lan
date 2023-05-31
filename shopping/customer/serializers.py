'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers
from customer.models import Customer


# 模型序列化器
class CustomerSerializer(serializers.ModelSerializer):
    # _authentication = serializers.JSONField(
    #     read_only=True
    # )
    first_name = serializers.CharField(
        # 是否必填
        required=True,
        # 是否可以为null
        allow_null=False,
        allow_blank=False,
        max_length=200,
    )
    last_name = serializers.CharField(
        # 是否必填
        required=True,
        # 是否可以为null
        allow_null=False,
        allow_blank=False,
        max_length=200,
    )
    phone = serializers.CharField(
        # 是否必填
        required=True,
        # 是否可以为null
        allow_null=False,
        allow_blank=False,
        max_length=200,
    )
    email = serializers.EmailField(
        # 是否必填
        required=True,
        # 是否可以为null
        allow_null=False,
        allow_blank=False,
        max_length=200,
        # 自定义错误提示
        error_messages={
            # 数据无效
            'invalid': 'error email',
            # 为空时错误提示
            'null': 'can not allow null'
        }
    )

    class Meta:
        model = Customer
        # 设置你需要的字段
        # fields = []
        fields = '__all__'
        # 除了某字段不要，其他都要
        # ecclude = []
