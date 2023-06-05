from django.db import models
from utils.base_model import BaseModel


# Create your models here.

class Authentication(BaseModel):
    password = models.CharField(default='', null=False, blank=False, max_length=200)
    password_confirmation = models.CharField(default='', null=True, blank=True, max_length=200)
    force_reset = models.BooleanField(default=False)

    def __str__(self):

        return self.password

    class Meta:
        db_table = 'authentication'


class Customer(BaseModel):
    # 数据中字段，默认会给一个id主键
    first_name = models.CharField(default='', null=False, blank=False, max_length=200)
    last_name = models.CharField(default='', null=False, blank=False, max_length=200)
    phone = models.CharField(default='', null=False, blank=False, max_length=200)
    email = models.CharField(default='', null=False, blank=False, max_length=200)
    company = models.CharField(default='', null=True, blank=True, max_length=200)
    store_credit = models.IntegerField(default=0, null=True, blank=True)
    registration_ip_address = models.CharField(default='', null=True, blank=True, max_length=200)
    customer_group_id = models.IntegerField(default=0, null=True, blank=True)
    notes = models.CharField(default='', null=True, blank=True, max_length=200)

    # 关系
    authentication = models.OneToOneField(to=Authentication, on_delete=models.DO_NOTHING, null=True)

    # def __str__(self):
    #     return self.id

    # 该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
