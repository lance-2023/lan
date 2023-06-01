from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
from test1.models import Book
from test1.ser import BookSerializer


# class BooksView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         bookSerializer = BookSerializer(books, many=True)
#         print(bookSerializer.data)
#         return Response(bookSerializer.data)
#
#
# class BookView(APIView):
#     def get(self, request, pk):
#         book = Book.objects.filter(id=pk).first()
#         bookSerializer = BookSerializer(book, many=True)
#         return Response(bookSerializer.data)
class BookViewSet(ModelViewSet):
    queryset = Book.objects
    serializer_class = BookModelSerializer
