from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.comment
