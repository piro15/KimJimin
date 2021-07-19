from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # 뷰가 호출돼서 프로필 템플릿 보여주는 건 로그인 된 상황에 국한되게.
# 로그인 안된 상태면 로그인 페이지로.
def profile(request):
    return render(request, 'accounts/profile.html')
