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

        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand

        fields = '__all__'


# 模型序列化器
class ProductSerializer(serializers.ModelSerializer):
    tax = TaxSerializer()
    category = CategorySerializer()
    brand = BrandSerializer()

    def create(self, validated_data):
        tax_name = validated_data.pop('tax')
        category_data = validated_data.pop('category')
        brand_data = validated_data.pop('brand')

        customer = Customer.objects.filter(id=customer_id).first()

        cart = Cart.objects.create(**validated_data, customer=customer)
        print(type(line_items_data))


        for line_item in line_items_data:
            # 改写Line_items的创建方法添加product外键信息
            product_data = line_item.pop('product')
            product_id = product_data.get('id')
            product = Product.objects.filter(id=product_id).filter().first()
            # 可以增加查询不到的代码，此处先省略
            line_item_obj = Line_items.objects.create(product=product, **line_item)
            cart.line_items.add(line_item_obj)


        return cart

    class Meta:
        model = Product
        # 设置你需要的字段
        # fields = []
        fields = '__all__'
        # 除了某字段不要，其他都要
        # exclude = []
