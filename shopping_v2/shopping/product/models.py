from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from utils.base_model import BaseModel


# Create your models here.
class Tax(BaseModel):
    tax_name = models.CharField(default='', null=True, blank=True, max_length=200)
    tax = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'tax'


class Category(BaseModel):
    category = models.CharField(default='', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'category'


class Brand(BaseModel):
    brand = models.CharField(default='', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'brand'


class Product(BaseModel):
    # 数据中字段，默认会给一个id主键
    name = models.CharField(default='', null=False, blank=False, max_length=200)
    type = models.CharField(default='', null=False, blank=False, max_length=20)
    sku = models.CharField(default='', null=True, blank=True, max_length=200)
    description = models.TextField(default='', null=True, blank=True, max_length=1000)
    weight = models.IntegerField(default=0, null=False, blank=False)
    width = models.IntegerField(default=0, null=True, blank=True)
    depth = models.IntegerField(default=0, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    search_keywords = models.CharField(default='', null=True, blank=True, max_length=200)
    images = models.JSONField(default=dict, null=True, blank=True)
    videos = models.JSONField(default=dict, null=True, blank=True)
    total_sold = models.IntegerField(default=0, null=True, blank=True)
    view_count = models.IntegerField(default=0, null=True, blank=True)

    # 关系
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)

    # 该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
