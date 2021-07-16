from django.db import models

# Create your models here.


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # Post 삭제하면 관련 댓글도 다 삭제.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
