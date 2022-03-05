from rest_framework import serializers

from api import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        exclude = ['author', ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleDetail
        exclude = ['article', ]


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class PageArticleSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='articledetail.content')
    author = serializers.CharField(source='author.username')
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = models.Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ['user']
