from django.conf import settings
from django.db import models
from django.utils import timezone
# 모든 모델 객체는 여기서 선언해서 먄든다. 모델이란 데이터 구조.
# 질문 모델, 답변 모델 등 원하는 형태의 모델을, 데이터 구조를 만드는 곳.


# 모델 정의. 객체 정의+모델 이름+상속. models.Model상속. 얘는 장고 모델이다.라고 알려주는 것.
class Post(models.Model):
    # 이 모델은 블로그 글 모델. 속성은 글쓴이, 제목, 내용 등.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # title, text 둘 다 텍스트 입력인데, title은 글자수 제한을 넣고 싶고. text는 그렇지 않으니 각각 특성에 맞게 models.Charfield, models.TextField.
    text = models.TextField()
    # 이런 걸 통틀어서 모델 필드 타입이라고 부른다. 필드마다 고유 옵션 존재. 떄마다 알아보면서 작성.
    created_date = models.DateTimeField(
        default=timezone.now)  # 값 지정 안됐을 때 쓰일 디폴트 값 지정.
    published_date = models.DateTimeField(
        blank=True, null=True)  # blank True는 empty값 허용한다는 의미. 디폴트는 False. null도 마찬가지로 null 허용 여부.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 모델을 models.py에 만들었으면
# 터미널에서 migrations, migrate 실행해서 만든 거 알려주기,
# 그리고 나서 admin,py에 가서 모델 클래스 등록
