'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers

from product.models import Product, Tax, Category, Brand


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax

        exclude = ['created_at', 'update_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        exclude = ['created_at', 'update_at']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand

        exclude = ['created_at', 'update_at']


# 模型序列化器
class ProductSerializer(serializers.ModelSerializer):
    tax = TaxSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    tax_id = serializers.IntegerField(write_only=True)
    category_id = serializers.IntegerField(write_only=True)
    brand_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        tax_id = validated_data.pop('tax_id')
        category_id = validated_data.pop('category_id')
        brand_id = validated_data.pop('brand_id')

        product = Product.objects.create(brand_id=brand_id, tax_id=tax_id, category_id=category_id, **validated_data)

        return product

    class Meta:
        model = Product
        # 设置你需要的字段
        # fields = []
        exclude = ['created_at', 'update_at']
        # 除了某字段不要，其他都要
        # exclude = []
