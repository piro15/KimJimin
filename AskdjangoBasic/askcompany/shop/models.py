from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # 객체 출력하고 싶을 때. 클래스에 대한 문자열 표현이 필요할 때
        # return self.name
        return f'<{self.pk}> {self.name}'.format(self.pk, self.name)
