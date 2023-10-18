from rest_framework import serializers
from .models import Article


class ArticlelistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title')


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'