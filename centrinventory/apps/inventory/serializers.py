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
        
    def validate(self, data):
        articles = data.get('ordering_articles')
        for article in articles:
            article_obj = article.get('article')
            amount = article.get('amount')
            if article_obj.stock < amount:
                raise serializers.ValidationError(f"There is not enough stock for the product {article_obj.name}")
            
        return super().validate(data)

    def create(self, validated_data):
        articles = validated_data.pop('ordering_articles')
        order = super().create(validated_data)
        for article in articles:
            article_obj = article['article']
            total_price = self.total_price(
                article['amount'], article_obj.price)
            total_price_vat = self.vat(
                total_price, article_obj.vat)+total_price
            OrderingArticle.objects.create(
                ordering=order, total_price=total_price, total_price_vat=total_price_vat, **article)
            article_obj.save()
        return order
    
    def update(self, instance, validated_data):
        articles = validated_data.pop('ordering_articles')
        instance = super().update(instance, validated_data)
        OrderingArticle.objects.filter(ordering=instance).delete()
        for article in articles:
            article_obj = article['article']
            total_price = self.total_price(
                article['amount'], article_obj.price)
            total_price_vat = self.vat(
                total_price, article_obj.vat)+total_price
            OrderingArticle.objects.create(
                ordering=instance, total_price=total_price, total_price_vat=total_price_vat, **article)
            article_obj.save()
        return instance

    def total_price(self, amount, price):
        return amount * price

    def vat(self, total_price, vat):
        return (vat / 100) * total_price
