import re
from django.shortcuts import get_object_or_404, redirect, render
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

# request.GET request.POST request.FILES


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })


def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_publish = data.get('is_publish') in (True, 't', 'True', '1')

        if len(name) < 2:
            error_list.append('name을 2글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_publish = is_publish

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_publish': is_publish,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                'is_publish': item.is_publish,
            }

    return render(request, 'shop/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)
