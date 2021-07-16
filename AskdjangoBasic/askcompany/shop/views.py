from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Item

# Create your views here.


def item_list(request):  # 함수를 만들어서
    # 아이템이라는 클래스를 통해 데이터베이스 접근 가능. 모든 아이템 목록을 가져와라X 가져올 준비 해라. 실제 가져오는 건 나중에 쿼리셋으로 레코드에 접근할 때.
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {  # httpresponse 타입의 객체 생성. 함수를 통해.
        'item_list': qs
    })


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))
