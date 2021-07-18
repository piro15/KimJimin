# from django.conf import settings
from django.db import models
from django.urls import reverse
from askcompany.utils import uuid_upload_to


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # 객체 출력하고 싶을 때. 클래스에 대한 문자열 표현이 필요할 때
        # return self.name
        return f'<{self.pk}> {self.name}'.format(self.pk, self.name)

    def get_absolute_url(self):
        # return reverse('shop:item_detail', args=[self.pk]
        return reverse('shop:item_detail', kwargs={'pk': self.pk})

# 정렬 지정: 모델 클래스 만들 때 같이 하는 걸 추천.
    # 이 방법이 default 설정하는 거라서 만약 orderby 나중에 넣어주면 그거 따라 실햄.


# delete함수 호출 반환값: 삭제된 record 갯수.
    # 왜 딕셔너리로 그런 값을 반환하느냐: 포스트, 댓글 있다고 생각. 포스트 지우면 댓글도 같이 삭제. 댓글까지 포함한 개수와, 댓글 모델과 댓글의 삭제 개수, 글 모델과 글 삭제 개수.
    # 총, 각 모델과 삭제 개수
    # delete할 때도 가급적 쿼리셋사용하기.

# RDBMS에서 1:N, M:N 헷갈릴 때 역으로 생각해도 성립되면 후자. 아니면 전자

# class Post(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
