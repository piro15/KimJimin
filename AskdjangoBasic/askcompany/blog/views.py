from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html')


# 뷰에 템플릿 경로 코드 분명 작성했고 template파일 추가도 했는데 템플릿 없다고 나오면
# 1.오타
# 2. 템플릿 만들어지고 나서 장고 개발 서버 시작된 적이 없을 때 .->장고 서버는 디렉토리 존재를 모른다.
# -> 서버 껐다가 다시 켜기
