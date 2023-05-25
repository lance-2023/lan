from django.db import models
from utils.base_model import  BaseModel

# Create your models here.
class Customer(BaseModel):
    #数据中字段，默认会给一个id主键
    _authentication = models.JSONField(default={})
    company = models.CharField(default='', max_length=200)
    first_name = models.CharField(default='', null=False, blank=False, max_length=200)
    last_name = models.CharField(default='', null=False, blank=False, max_length=200)
    phone = models.CharField(default='', null=False, blank=False, max_length=200)
    email = models.CharField(default='', null=False, blank=False, max_length=200)
    store_credit = models.IntegerField(default=0)
    registration_ip_address = models.CharField(default='', max_length=200)
    customer_group_id = models.IntegerField(default=0)
    notes = models.CharField(default='', max_length=200)
    tax_exempt_category = models.CharField(default='', max_length=200)

    #该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'