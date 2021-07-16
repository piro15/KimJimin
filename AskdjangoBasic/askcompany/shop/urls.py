from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views
register_converter(FourDigitYearConverter, 'yyyy')
app_name = 'shop'


urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('items/', item_list, name='item_list'),
    # ~~items/라는 주소에 매칭이되면 item_list라는 이름의 함수를 호춣을 하겠다. 이때 이런 패턴의 이름을 item_list라고 하겠다.

]
