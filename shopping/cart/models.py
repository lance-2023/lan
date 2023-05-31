import uuid

from django.db import models
from utils.base_model import  BaseModel

# Create your models here.
class Cart(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=200, default=uuid.uuid4(), editable=False)
    line_item = models.JSONField(default=dict, null=False, blank=False)
    custom_items = models.JSONField(default=dict)
    gift_certificates = models.JSONField(default=dict)
    customer_id = models.IntegerField(default=0)
    channel_id = models.IntegerField(default=0)
    currency = models.JSONField(default=dict)
    locale = models.CharField(default='', max_length=200)
    email = models.CharField(default='', max_length=200)
    tax_included = models.BooleanField(default=False)
    discount_amount = models.IntegerField(default=0)
    cart_amount = models.IntegerField(default=0)
    discounts = models.JSONField(default=dict)
    coupons = models.JSONField(default=dict)

    #该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
