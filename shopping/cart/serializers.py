"""
author:lance.lan
date:2023/5/24
project:djangoProject
"""
from rest_framework import serializers
from cart.models import Cart
from customer.serializers import CustomerSerializer
from order.models import Line_items, Discounts
from order.serializers import DiscountsSerializer, Line_itemsSerializer
from product.models import Product


# 模型序列化器
class CartSerializer(serializers.ModelSerializer):
    line_items = Line_itemsSerializer(many=True)
    # discounts = DiscountsSerializer(many=True)

    # 只在序列化使用
    customer = CustomerSerializer(read_only=True)

    # 1、由于在Customer的模型中重写了__str__所以返回值就是customer的id
    # customer_id = serializers.IntegerField(source='customer.id')
    customer_id = serializers.IntegerField()

    # 2、line_items是个多对多，返回值肯定要用serializers.SerializerMethodField()
    # line_items = serializers.SerializerMethodField()
    #
    # def get_line_items(self, obj):
    #     return {
    #         [{'quantity': obj_line_item.line_item.quantity,
    #           'product_id': obj_line_item.line_item.product.id}
    #          for obj_line_item in obj.line_items.all()]
    #     }

    # 2、discounts是个多对多，返回值肯定要用serializers.SerializerMethodField
    # # discounts =
    # def get_discounts(self, obj):
    # discounts = serializers.SerializerMethodField()

    # def get_discounts(self, obj):
    #     return {
    #         [{'name': obj_discount.discount.name,
    #           'discount': obj_discount.discount.discount}
    #          for obj_discount in obj.discounts.all()
    #          ]
    #     }

    # def create(self, validated_data):
    #     # 建立line_items和discounts的多对多，以及customer的外键（创建时需要传入Customer对象）
    #     # 建立line_items和discounts的多对多，以及customer的外键（创建时需要传入Customer对象）
    #     # 前端传回的line_items数据，先建立line_items对象，再建立cart对象
    #
    #     # discounts_data = validated_data.pop('discounts')
    #     print(validated_data)
    #     customer = validated_data.pop('customer')
    #
    #     line_items_data = validated_data.pop('line_items')
    #     customer = Customer.objects.filter(id=customer.get('id')).first()
    #
    #     cart = Cart.objects.create(**validated_data, customer=customer)
    #     print(line_items_data)
    #     for line_item in line_items_data:
    #         # 改写Line_items的创建方法添加product外键信息
    #         print(*line_item)
    #         line_item_obj = Line_items.objects.create(**line_item)
    #         line_item_obj = Line_items.objects.create(product_id=line_item["product"].get('id'), quantity=line_item["quantity"])
    #         cart.line_items.add(line_item_obj)
    #     # discounts = Discounts.objects.create(**discounts_data)
    #     # for discount in discounts_data:
    #     #     # 改写Line_items的创建方法添加product外键信息
    #     #     discount_obj = Discounts.objects.create(**discount)
    #     #     cart.discounts.add(discount_obj)
    #
    #     return cart

    def create(self, validated_data):
        # 建立line_items和discounts的多对多，以及customer的外键（创建时需要传入Customer对象）
        # 前端传回的line_items数据，先建立line_items对象，再建立cart对象
        print(validated_data)

        # discounts_data = validated_data.pop('discounts')
        customer_data_id = validated_data.pop('customer_id')
        print(customer_data_id)
        line_items_data = validated_data.pop('line_items')
        print(line_items_data)

        # customer = Customer.objects.filter(id=customer_id).first()

        cart = Cart.objects.create(**validated_data, customer_id=customer_data_id)
        print(type(line_items_data))

        # line_item = line_items_data[0]
        # product = line_item.pop('product')
        # print(product)
        # product_id = product.get('id')
        # print(product_id)

        for line_item in line_items_data:
            # 改写Line_items的创建方法添加product外键信息
            product_data = line_item.pop('product')
            product_id = product_data.get('id')
            product = Product.objects.filter(id=product_id).filter().first()
            # 可以增加查询不到的代码，此处先省略
            line_item_obj = Line_items.objects.create(product=product, **line_item)
            cart.line_items.add(line_item_obj)
        # discounts = Discounts.objects.create(**discounts_data)
        # for discount in discounts_data:
        #     # 改写Line_items的创建方法添加product外键信息
        #     discount_obj = Discounts.objects.create(**discount)
        #     cart.discounts.add(discount_obj)
        print(cart.customer_id)

        return cart

    class Meta:
        model = Cart
        # 设置你需要的字段
        exclude = ['created_at', 'update_at']
