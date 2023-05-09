from typing import Iterable, Optional
from django.db import models

# Create your models here.


class Article(models.Model):
    reference = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    vat = models.FloatField()
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()


class Ordering(models.Model):
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)


class OrderingArticle(models.Model):
    ordering = models.ForeignKey(
        Ordering, related_name="ordering_articles", on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, related_name="article_orders", on_delete=models.CASCADE)
    amount = models.IntegerField()
    total_price = models.FloatField(null=True, blank=True)
    total_price_vat = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        article = self.article
        total = self.article.stock - self.amount
        if total < 0:
            ValueError
        else:
            self.article.stock = total
        super(OrderingArticle,self).save(*args, **kwargs)