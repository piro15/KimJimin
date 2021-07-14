# 장고의 관리자 기능에 대한 설정, 앱-관리자 기능 연결.

from django.contrib import admin
# models.py에서 모델 클래스 만들고 migrate 하고 나서 admin.py에 불러오기.
from .models import Post

admin.site.register(Post)  # 관리자 페이지에서 만든 모델 보려고 등록.
