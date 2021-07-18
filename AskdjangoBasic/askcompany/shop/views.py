from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Item
# from shop.models import Item

# Create your views here.


# def item_list(request):  # 함수를 만들어서
#     # 아이템이라는 클래스를 통해 데이터베이스 접근 가능. 모든 아이템 목록을 가져와라X 가져올 준비 해라. 실제 가져오는 건 나중에 쿼리셋으로 레코드에 접근할 때.
#     qs = Item.objects.all()
#     return render(request, 'shop/item_list.html', {  # httpresponse 타입의 객체 생성. 함수를 통해.
#         'item_list': qs
#     })


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()  # 가져올 예정이다

    q = request.GET.get('q', '')  # GET인자에서 값을 하나 가져온다. q를 가져오는데 없으면 빈문자열 반환
    if q:  # 검색어가 있다먄
        qs = qs.filter(name__icontains=q)  # 대소문자 구분 안하겠다.

    return render(request, 'shop/item_list.html', {  # 그냥 item_list말고 shop/꼭 붙여줘야 한다.
        'item_list': qs,  # 템플릿은 item_list로 qs를 참조하겠다
        'q': q,
    })

# render는 HttpResponse 반환. 템플릿 찾아달라는 요청.
# 인자는 request, template_name, context(주로 딕셔너리 형태),
#   content_type(text/html, text/css, text/javascript),
#   status(200,300,404,500...),
#   using(템플릿 엔진 지정. 지정 안하면 기본인 장고 템플릿 엔진.)

# 프로젝트 디렉토리 주소 뒤에 붙여서 매칭 시도. 없으면 각 앱 디렉토리 주소 뒤에 붙여서 매칭 시도. 마지막 앱까지 시도했는데 못 찾으면 찾을 수 없다고 출력.


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })
