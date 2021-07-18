# from django.conf import settings

from django.db import models
from askcompany.utils import uuid_upload_to
# Create your models here.


class Post(models.Model):
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # Post 삭제하면 관련 댓글도 다 삭제.
    # CASCADE, SET_NULL, SET이 세 가지가 주로 쓰임.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()


# user 모델 임포트해서 직접 사용하지 말고 setting.AUTH_USER_MODEL로 쓰기.
# 장고의 유저 모델은 변경 가능. 후자 방법으로 하면 변경했을 때 지정돼있는 디폴트 값으로 변경되기 떄문에. 훨씬 유연.
# Post.objects.filter(author=user)

# 15강 7페이지 reverse_name아니고 related_name

# from blog.models import Post, Comment
# Post.objects.all().count()

# Post.objects.create(author_name='user1',title='title1',content='content1')

# Profile.objects.get(author=user)

# post-tag article-tag 면 tag를 독립적으로 쓰고 post,article에 ManyToMany쓰기.
