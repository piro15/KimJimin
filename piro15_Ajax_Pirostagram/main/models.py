from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    like = models.BooleanField(null=True)


class Comment(models.Model):
    # 같은 앱 내에서는 main.~말고 그냥~
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField(null=True)
