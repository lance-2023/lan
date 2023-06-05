'''
author:lance.lan
date:2023/5/24
project:djangoProject
'''
from rest_framework import serializers

from customer.models import Customer
from customer.serializers import CustomerSerializer
from order.models import Order, Discounts, Shipping_address, Billing_address, Line_items
from product.models import Product


# 模型序列化器
class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts

        fields = '__all__'


class Line_itemsSerializer(serializers.ModelSerializer):
    # 前端传过来的product_id信息会被解构成('product', {'id': 1})，其实就是product.id
    product_id = serializers.IntegerField(source='product.id')

    class Meta:
        model = Line_items

        fields = ['product_id', 'quantity']


class Shipping_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_address

        fields = '__all__'


class Billing_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing_address

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = Line_itemsSerializer(many=True)
    billing_address = Billing_addressSerializer()
    shipping_address = Shipping_addressSerializer()
    # 只在序列化使用
    customer = CustomerSerializer(read_only=True)
    # 只在反序列化使用
    customer_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        print(validated_data)
        billing_address_data = validated_data.pop('billing_address')
        shipping_address_data = validated_data.pop('shipping_address')
        customer_id = validated_data.pop('customer_id')

        products_data = validated_data.pop('products')
        print(products_data)

        customer = Customer.objects.filter(id=customer_id).first()
        print(customer)

        print(billing_address_data)
        billing_address = Billing_address.objects.create(**billing_address_data)
        print(billing_address)

        print(shipping_address_data)
        shipping_address = Shipping_address.objects.create(**shipping_address_data)
        print(shipping_address)

        order = Order.objects.create(**validated_data, customer=customer, shipping_address=shipping_address,
                                     billing_address=billing_address)

        for product_data in products_data:
            product_id = product_data.pop('product').get('id')
            product = Product.objects.filter(id=product_id).filter().first()
            # 可以增加查询不到的代码，此处先省略
            product_obj = Line_items.objects.create(product=product, **product_data)
            order.products.add(product_obj)

        return order

    class Meta:
        model = Order
        # 设置你需要的字段
        # fields = []
        fields = '__all__'  # 除了某字段不要，其他都要
        # exclude = []
