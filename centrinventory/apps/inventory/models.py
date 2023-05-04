from typing import Iterable, Optional
from django.db import models

# Create your models here.


class Article(models.Model):
    reference = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    vat = models.FloatField()
    creation_date = models.DateField(auto_created=True)
    stock = models.IntegerField()


class Ordering(models.Model):
    total_price = models.FloatField()
    total_price_vta = models.FloatField()
    creation_date = models.DateField(auto_created=True)


class OrderingArticle(models.Model):
    ordering = models.ForeignKey(
        Ordering, related_name="ordering_articles", on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, related_name="article_orders", on_delete=models.CASCADE)
    cant = models.IntegerField()
