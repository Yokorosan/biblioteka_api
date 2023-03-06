from django.shortcuts import render
from rest_framework import generics
from .models import Book, BookCopy
from .serializers import BookSerializer

# Create your views here.


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"


class BookCopyView(generics.CreateAPIView):
    ...


class BookCopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...
