from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views
register_converter(FourDigitYearConverter, 'yyyy')
app_name = 'shop'


urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    # path('items/', item_list, name='item_list'),
    # # ~~items/라는 주소에 매칭이되면 item_list라는 이름의 함수를 호춣을 하겠다. 이때 이런 패턴의 이름을 item_list라고 하겠다.

]


# HTTP 상태코드:
# 모두 다 200으로 통일시키는 곳도 있지만 경우에 맞게 각각 다른 응답을 보내는 것이 좋다. REST API에 특히 좋다는데 과제 다 하고 REST API가 뭔지 찾아보기
# HttpResopnse 쓸 때 status 변경하고 싶으면 콤마 쓰고 스테이터스 =~~.

# resolve_url('shop:item_list') 패턴네임이 item_list인 애의 url을 찾아준다
# resolve_url 쓰는 두 줄이 redirect쓰는 한 줄과 같다. 그러니 후자 쓰는 게 더 좋다.

# Http404쓸 거면 raise. HttpResponseNotFound 쓸 거면 return. 하지만 후자는 잘 쓰지X


# 그냥 python3, exit() 이거 말고
# python3 manage.py shell 쓰기
# 전자: 장고 초기화 과정..?이 없어서 오류 뜬다. 할 수는 있다. 근데 번거롭다. 코드는 pdf에. 또는 --help에서 명령 추가

# 파이프 명령 | 두 명령어 이어주기. 앞 명령의 표준 출력을 뒷 명령의 표준 입력으로 넣어준다.
