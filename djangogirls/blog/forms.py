# 강력한 인터페이스 제작. 상상할 수 있는 모든 것 구현 가능

from django import forms

from .models import Post


class PostForm(forms.ModelForm):  # PostForm이 만들 폼의 이름, 이 폼이 ModelForm이다.

    class Meta:
        model = Post  # 이 폼 만들려면 필요한 모델 무엇.
        fields = ('title', 'text',)
