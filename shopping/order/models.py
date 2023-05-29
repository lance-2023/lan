from django.db import models
from utils.base_model import  BaseModel

# Create your models here.
class Order(BaseModel):
    #数据中字段，默认会给一个id主键
    billing_address = models.JSONField(default=dict, null=False, blank=False)
    products = models.JSONField(default=dict, null=True, blank=True)
    consignments = models.JSONField(default=dict, null=True, blank=True)

    shipping_addresses = models.JSONField(default=dict, null=True, blank=True)
    status_id = models.IntegerField(default=0, null=True, blank=True)
    base_handling_cost = models.IntegerField(default=0, null=True, blank=True)
    base_shipping_cost = models.IntegerField(default=0, null=True, blank=True)
    base_wrapping_cost = models.IntegerField(default=0, null=True, blank=True)
    channel_id = models.IntegerField(default=0, null=True, blank=True)
    customer_id = models.IntegerField(default=0, null=True, blank=True)
    customer_message = models.CharField(default='', max_length=200, null=True, blank=True)

    default_currency_code = models.IntegerField(default=0, null=True, blank=True)
    discount_amount = models.IntegerField(default=0, null=True, blank=True)
    geoip_country = models.CharField(default='', max_length=200, null=True, blank=True)
    customer_locales = models.CharField(default='', max_length=200, null=True, blank=True)
    ip_address = models.CharField(default='', max_length=200, null=True, blank=True)
    is_deleted = models.IntegerField(default=0, null=True, blank=True)
    items_shipped = models.IntegerField(default=0, null=True, blank=True)
    items_total = models.IntegerField(default=0, null=True, blank=True)
    order_is_digital = models.IntegerField(default=0, null=True, blank=True)
    payment_method = models.CharField(default='', max_length=200, null=True, blank=True)
    payment_provider_id = models.IntegerField(default=0, null=True, blank=True)
    subtotal_ex_tax = models.IntegerField(default=0, null=True, blank=True)
    subtotal_inc_tax = models.IntegerField(default=0, null=True, blank=True)


    #该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'