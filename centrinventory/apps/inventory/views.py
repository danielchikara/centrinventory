from django.shortcuts import render
from rest_framework import generics
from apps.inventory.serializers import *
from apps.inventory.models import *


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class UpdateArticle(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ListArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class RetrieveArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CreateOrder (generics.CreateAPIView):
    serializer_class = OrderingSerializer


class UpdateOrder(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class RetrieveOrder(generics.RetrieveAPIView):
    serializer_class = OrderingSerializer
    queryset = Ordering.objects.all()


class ListOrder(generics.ListAPIView):
    serializer_class = OrderingSerializer
    queryset = Ordering.objects.all()
