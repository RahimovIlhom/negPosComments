from django.urls import path
from negPosAPI.views import CommentViewSet

urlpatterns = [
    path('articles/<int:article_id>/comments', CommentViewSet.as_view({'post': 'create'})),
    path('articles/<int:article_id>/comments/', CommentViewSet.as_view({'post': 'create'})),
]