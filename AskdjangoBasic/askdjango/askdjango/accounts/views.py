from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import CreateView
from .forms import SignupForm


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)  # 회원가입 제대로 했으면 로그인 페이지
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

signup = CreateView.as_view(model=User,
                            form_class=SignupForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')


@login_required  # 뷰가 호출돼서 프로필 템플릿 보여주는 건 로그인 된 상황에 국한되게.
# 로그인 안된 상태면 로그인 페이지로.
def profile(request):
    return render(request, 'accounts/profile.html')
