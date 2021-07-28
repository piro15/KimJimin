from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Post 모델 속성들 중에서 form에 보여주고 싶은 것만
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'  # 전체 필드
