'''
author:lance.lan
date:2023/6/1
project:djangoProject
'''
from django.urls import path, re_path
from test1 import views

urlpatterns = [
    # path("books/", views.BooksView.as_view()),
    # re_path("books/(?P<pk>\d+)", views.BookView.as_view())

    path("books/", views.BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path("^books/(?P<pk>\d+)", views.BookViewSet.as_view({'get': 'retrieve',
                                                            'put': 'update',
                                                            'delete': 'destroy'}))
]
