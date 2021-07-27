from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
    post = Post.objects.all()
    ctx = {'post': post}
    return render(request, 'main/post_list.html', ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}
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
