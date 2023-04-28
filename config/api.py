from rest_framework import routers
from accounts.views import UserViewSet
from negPosAPI.views import ArticleViewSet, CommentViewSet, NegativeCommentViewSet, PositiveCommentViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'negative-comments', NegativeCommentViewSet, basename='negative-comment')
router.register(r'positive-comments', PositiveCommentViewSet, basename='positive-comment')