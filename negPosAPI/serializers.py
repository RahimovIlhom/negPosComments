from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer


class ArticleSerializers(serializers.ModelSerializer):
    # author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Article
        fields = ['id', 'author_id', 'title', 'summary', 'photo', 'body', 'date', 'comments', 'url']
        write_only_fields = ['author_id']


class CommentSerializers(serializers.ModelSerializer):
    # author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # article = ArticleSerializers(
    #     many=False,
    #     required=False
    # )
    # url = serializers.HyperlinkedIdentityField(view_name='comment-detail')

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'type', 'author_id', 'article_id', 'created_at', 'url']
        write_only_fields = ['author_id', 'article_id']
