from rest_framework import serializers
from apps.inventory.models import *


class ArticleSerializer(serializers.ModelSerializer):
    article_creation_date = serializers.ReadOnlyField(source="creation_date")

    class Meta:
        model = Article
        exclude = ('creation_date',)


class ArticleSerializerOrder(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    article = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all())
    
    class Meta:
        model = OrderingArticle
        fields = ['article', 'amount','total_price','total_price_vat']


class OrderingSerializer(serializers.ModelSerializer):
    articles = ArticleSerializerOrder(source="ordering_articles",
                                      many=True)

    class Meta:
        model = Ordering
        exclude = ('creation_date',)

    def create(self, validated_data):
        articles = validated_data.pop('ordering_articles')
        order = super().create(validated_data)
        for article in articles:
            total_price = self.total_price(
                article['amount'], article['article'].price)
            total_price_vat = self.vat(
                total_price, article['article'].vat)+total_price
            OrderingArticle.objects.create(
                ordering=order, total_price=total_price, total_price_vat=total_price_vat, **article)
        return order

    def total_price(self, amount, price):
        return amount * price

    def vat(self, total_price, vat):
        return (vat / 100) * total_price
