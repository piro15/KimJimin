from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm
# Create your views here.


def post_list(request):
    posts = Post.objects.all()  # 단복수형 맞게.
    ctx = {'posts': posts}
    return render(request, 'main/post_list.html', ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    ctx = {'post': post,
           'comments': comments,
           }
    return render(request, 'main/post_detail', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {'form': form}
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {'form': form, }
        return render(request, 'main/post_new.html', ctx)
