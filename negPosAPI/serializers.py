from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer


class ArticleSerializers(serializers.ModelSerializer):
    author = UserSerializer(
        many=False,
        required=False
        )
    # comments = CommentSerializers(
    #     many=True,
    #     required=False
    # )

    class Meta:
        model = Article
        fields = ['url', 'id', 'author', 'title', 'summary', 'photo', 'body', 'date', 'comments']


class CommentSerializers(serializers.ModelSerializer):
    article = ArticleSerializers(
        many=False,
        required=False
    )
    author = UserSerializer(
        many=False,
        required=False
    )

    class Meta:
        model = Comment
        fields = ['url', 'article', 'comment', 'author', 'type']
