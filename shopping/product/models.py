from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from utils.base_model import  BaseModel

# Create your models here.
class Product(BaseModel):
    #数据中字段，默认会给一个id主键
    name = models.CharField(default='', null=False, blank=False, max_length=200)
    type = models.CharField(default='', null=False, blank=False, max_length=20)
    sku = models.CharField(default='', max_length=200, null=True, blank=True)
    description = models.TextField(default='', max_length=1000, null=True, blank=True)
    weight = models.IntegerField(default=0, null=False, blank=False)
    width = models.IntegerField(default=0, null=True, blank=True)
    depth = models.IntegerField(default=0, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=False, blank=False)

    categories = models.JSONField(default=dict, null=True, blank=True)
    brand_id = models.IntegerField(default=0, null=True, blank=True)
    tax_class_id = models.IntegerField(default=0, null=True, blank=True)
    open_graph_type = models.CharField(default='', max_length=200, null=True, blank=True)
    open_graph_title = models.CharField(default='', max_length=200, null=True, blank=True)
    open_graph_description = models.CharField(default='', max_length=200, null=True, blank=True)

    open_graph_use_meta_description = models.BooleanField(default=False)
    open_graph_use_product_name = models.BooleanField(default=False)
    open_graph_use_image = models.BooleanField(default=False)
    is_free_shipping = models.BooleanField(default=False)
    is_visibleb = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    related_products = models.JSONField(default=dict, null=True, blank=True)
    search_keywords = models.CharField(default='', max_length=200, null=True, blank=True)

    images = models.JSONField(default=dict, null=True, blank=True)
    videos = models.JSONField(default=dict, null=True, blank=True)

    layout_file = models.CharField(default='', max_length=200, null=True, blank=True)

    total_sold = models.IntegerField(default=0, null=True, blank=True)
    view_count = models.IntegerField(default=0, null=True, blank=True)
    reviews_count = models.IntegerField(default=0, null=True, blank=True)

    #custom_field,id;name,string,required;value,string,required
    custom_fields = models.JSONField(default=dict, null=True, blank=True)
    #批量定价规则。id，integer，required；quantity_min，integer，required；quantity_max，integer，required；type，string，required；amount，required
    bulk_pricing_rules = models.JSONField(default=dict, null=True, blank=True)


    #该模型的元数据，用于描述该模型
    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'