import uuid

from django.db import models

from customer.models import Customer
from utils.base_model import BaseModel
from order.models import Discount

from product.models import Product


# Create your models here.

class Cart(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=200, default=uuid.uuid4(), editable=False)
    channel_id = models.IntegerField(default=0, null=True, blank=True)
    currency = models.CharField(default='', null=True, blank=True, max_length=200)
    locale = models.CharField(default='', null=True, blank=True, max_length=200)

    # 关系
    line_item = models.ManyToManyField(to=Product, null=True)
    discounts = models.ManyToManyField(to=Discount, null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING, null=True)

    # 该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
