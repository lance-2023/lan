'''
author:lance.lan
date:2023/6/1
project:djangoProject
'''
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from test1.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(Serializer):
    # 其实是book.publish，而book.publish又返回的是def __str__(self)，因此可以通过修改返回值从而修改信息
    publish = serializers.CharField()

    # 通过source属性指定字段名，此时序列化器中的名称可以自定义，返回值不再是title而是not_title，从而保证了数据库字段名不被泄露

    not_title = serializers.CharField(source='title')
    # 1、一对多关系，外键联表查询，查询publish表
    publish_email = serializers.CharField(source='publish.email')

    # 2、多对多关系 SerializerMethodField必须配套一个（get_字段名）的方法
    authors = serializers.SerializerMethodField()

    def get_authors(self, instance):
        # 此处的instance就是一个Book对象，返回值就是显示的信息
        authors = instance.authors.all()
        # 基于对象的跨表查
        authors_list = []
        for author in authors:
            authors_list.append({'name': author.name, 'age': author.age})

        return authors_list
