from django.db import models

from customer.models import Customer
from product.models import Product
from utils.base_model import BaseModel


# Create your models here.
class Billing_address(BaseModel):
    first_name = models.CharField(default='', null=True, blank=True, max_length=200)
    last_name = models.CharField(default='', null=True, blank=True, max_length=200)
    company = models.CharField(default='', null=True, blank=True, max_length=200)
    street = models.CharField(default='', null=True, blank=True, max_length=200)
    city = models.CharField(default='', null=True, blank=True, max_length=200)
    state = models.CharField(default='', null=True, blank=True, max_length=200)
    country = models.CharField(default='', null=True, blank=True, max_length=200)
    phone = models.CharField(default='', null=True, blank=True, max_length=200)
    email = models.CharField(default='', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.first_name + self.last_name + self.email

    class Meta:
        db_table = 'billing_address'


class Shipping_address(BaseModel):
    first_name = models.CharField(default='', null=True, blank=True, max_length=200)
    last_name = models.CharField(default='', null=True, blank=True, max_length=200)
    company = models.CharField(default='', null=True, blank=True, max_length=200)
    street = models.CharField(default='', null=True, blank=True, max_length=200)
    city = models.CharField(default='', null=True, blank=True, max_length=200)
    state = models.CharField(default='', null=True, blank=True, max_length=200)
    country = models.CharField(default='', null=True, blank=True, max_length=200)
    phone = models.CharField(default='', null=True, blank=True, max_length=200)
    email = models.CharField(default='', null=True, blank=True, max_length=200)
    shipping_method = models.CharField(default='', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.first_name + self.last_name + self.email

    class Meta:
        db_table = 'shipping_address'


class Line_items(BaseModel):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'line_items'


class Discount(BaseModel):
    name = models.CharField(default='', null=True, blank=True, max_length=200)
    discount = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'discount'


class Order(BaseModel):
    # 数据中字段，默认会给一个id主键
    status_id = models.IntegerField(default=1, null=True, blank=True)
    order_is_digital = models.BooleanField(default=False)

    channel_id = models.IntegerField(default=0, null=True, blank=True)
    customer_message = models.CharField(default='', null=True, blank=True, max_length=200)

    geoip_country = models.CharField(default='', null=True, blank=True, max_length=200)
    customer_locales = models.CharField(default='', null=True, blank=True, max_length=200)
    ip_address = models.CharField(default='', null=True, blank=True, max_length=200)

    base_handling_cost = models.IntegerField(default=0, null=True, blank=True)
    base_shipping_cost = models.IntegerField(default=0, null=True, blank=True)
    base_wrapping_cost = models.IntegerField(default=0, null=True, blank=True)

    default_currency_code = models.CharField(default="CNY", null=True, blank=True, max_length=200)
    payment_method = models.CharField(default='', null=True, blank=True, max_length=200)
    payment_provider_id = models.IntegerField(default=0, null=True, blank=True)

    discounts = models.ManyToManyField(to=Discount, null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING, null=True)
    billing_address = models.ForeignKey(to=Billing_address, on_delete=models.DO_NOTHING, null=True)
    line_items = models.OneToOneField(to=Line_items, on_delete=models.DO_NOTHING, null=True)
    shipping_address = models.ForeignKey(to=Shipping_address, on_delete=models.DO_NOTHING, null=True)

    # 该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
