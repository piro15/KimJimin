from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.


def post_list(request):
    post = Post.objects.all()
    ctx = {'post': post}
    return render(request, 'main:post_list', ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}
    return render(request, 'main:post_detail', ctx)


def post_new(request, pk):
    return render(request, 'main:post_new')
