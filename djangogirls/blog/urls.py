from django.urls import path
from . import views
# urlresolver가 사용하는 패턴 목록. 웹브라우저가 웹서버에 요청하면 그 요청을 장고로 전달.
# 장고 urlresolver가 받은 url을 자신이 갖고 있는 아래 패턴 목록과 일일이 비교.
# 일치하는 거 찾으면 path 함수 인자로 써있는 뷰 함수에 넘겨준다.
# path 함수 필수 인자: route, view, 선택인자: kwargs, name
urlpatterns = [
    # ''이면 루트 URL. 루트 URL 들어왔을 때 view.post_list보여주기.
    path('', views.post_list, name='post_list'),

    # url 만들기. 루트 url+ 첫 번째 인자.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 장고 해당 url과 같은 이 줄을 찾아내고 post detail 뷰로 요청 넘겨준다.
    # views.post_detail이라는 뷰의 이름을 post_detail로.
    # <int:pk>: 정수값이 올 자리. pk 변수로 뷰에 전송한다.(pk는 각 튜플의 식별키.그러니 글마다 그 값이 다를 것. )
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # url 만들기. 루트 url+ 첫 번째 인자. 해당 url이 들어오면 두 번째 인자 뷰로 전송.

]
