from django.conf import settings
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render, resolve_url
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
#             auth_login(request, user)
#             return redirect('profile')  # 회원가입 제대로 했으면 로그인 페이지
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()


@login_required  # 뷰가 호출돼서 프로필 템플릿 보여주는 건 로그인 된 상황에 국한되게.
# 로그인 안된 상태면 로그인 페이지로.
def profile(request):
    return render(request, 'accounts/profile.html')
