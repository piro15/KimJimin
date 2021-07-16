import debug_toolbar
# from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
# 중단점 만들고 페이지 새로고침하면 응답X 실행 중인 부분 노란색으로 표시 . 디버깅에서 request, x,y값 보기 가능.
# 뭔가를 수정했으면 초록색 동그란 화살표 다시 누르기
