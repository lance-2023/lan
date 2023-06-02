'''
author:lance.lan
date:2023/5/25
project:shopping
'''
import time

from django.db import models


##基础模型，继承该模型后，会在创建和修改时增加时间字段
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # 所有的model在执行迁移的时候会新建表，如果加了abstract=True则不会生成表，表示模型是虚拟的，提供给别的表使用
    class Meta:
        abstract = True
