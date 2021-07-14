"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # path, include 함수 쓰려면 필요.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # url 확인. 찾기. view로 연결.
]

# URLconf url configuration.: url 커넥션 프로퍼티들의 집합. urls.py가 URLcof
# URL Uniform Resource Locators
