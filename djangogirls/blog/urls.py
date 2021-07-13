from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # url 만들어 장고가 post detail 뷰로 보내 게시글 보이게.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # views.post_detail이라는 뷰의 이름을 post_detail로.
    # post/ : url이 post 문자를 포함해야 한다.
    # <int:pk>: 정수값을 기대하고 이를 pk라는 변수로 뷰로 전송한다
    # /: 다음에 /가 한 번 더 온다
]
