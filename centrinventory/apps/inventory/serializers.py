from rest_framework import serializers
from apps.inventory.models import *

class ArticleSerializer(serializers.ModelSerializer):
    article_creation_date = serializers.ReadOnlyField(source="creation_date")
    class Meta:
        model = Article
        exclude = ('creation_date',)
    