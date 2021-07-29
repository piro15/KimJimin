from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.


def post_list(request):
    posts = Post.objects.all()  # 단복수형 맞게.
    ctx = {'posts': posts}
    return render(request, 'main/post_list.html', ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    ctx = {'post': post, 'comments': comments, }
    return render(request, 'main/post_detail.html', ctx)


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


def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('main:post_detail', pk)
    else:
        form = PostForm(instance=post)
        ctx = {'form': form}
        return render(request, template_name='main/post_new.html', context=ctx)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('main:post_list')


@csrf_exempt
def like_ajax(request):
    # 뷰에서 쓰려면 파이썬 객체로 가져와야 해서 파이썬 객체로 파싱해주는 json.loads 작성
    req = json.loads(request.body)
    post_id = req['id']
    type = req['type']
    post = Post.objects.get(id=post_id)
    if type == 'dislike':
        post.like = True
    else:
        post.like = False

    post.save()  # DB에 저장.

    return JsonResponse({'id': post_id, 'type': type})
    # 딕셔너리는 파이썬이니까 ajax 요청할 때는 JsonResponse
    # 요청이 왔던 곳으로 다시 보내준다.


@csrf_exempt
def new_comment(request):
    req = json.loads(request.body)
    post_id = req['id']
    content = req['content']
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(post=post, content=content)
    comment_id = comment.id
# https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/
# 두 번째 방법으로 하면 .save() 쓰지 X
    return JsonResponse({'id': post_id, 'content': content, 'comment_id': comment_id})


@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return JsonResponse({'id': comment_id})
