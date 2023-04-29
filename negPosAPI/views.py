from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .checkComment.checkComment import checkText
from .models import Article, Comment
from .pagination import CustomPagination
from .serializers import ArticleSerializers, CommentSerializers


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        page = CustomPagination
        serializers = ArticleSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        page = CustomPagination
        article = get_object_or_404(queryset, pk=pk)
        serilizers = ArticleSerializers(article, context=self.get_serializers_context())
        return Response(serilizers.data)

    def create(self, request):
        author = request.user
        article = Article.objects.create(
            author=author,
        )
        serializer = ArticleSerializers(article, data=request.data, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializers(article, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializers(article, partial=True, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_class = [IsAuthenticated]
        else:
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.all()
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        page = CustomPagination
        comment = get_object_or_404(queryset, pk=pk)
        serilizers = CommentSerializers(comment, context=self.get_serializers_context())
        return Response(serilizers.data)

    def create(self, request, *args, **kwargs):
        author = request.user
        article_id = kwargs.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        commentNew = Comment.objects.create(
            author=author,
            article=article
        )
        serializer = CommentSerializers(commentNew, data=request.data, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            commentNew.comment = serializer.validated_data['comment']
            checkC = checkText(commentNew.comment)
            if checkC['label'] == 1:
                commentNew.type = 'Positive'
            else:
                commentNew.type = 'Negative'
            commentNew.save()
            serializer = CommentSerializers(commentNew, context=self.get_serializers_context())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializers(comment, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializers(comment, partial=True, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}

    def get_permissions(self):
        if self.action == 'list' or self.action == 'create':
            permission_class = [IsAuthenticated]
        else:
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class NegativeCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='Negative')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='Negative')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}

    def get_permissions(self):
        permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class PositiveCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='Positive')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='Positive')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}

    def get_permissions(self):
        permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]
