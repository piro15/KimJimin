from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_new(request):
    if request.method == "POST":  # method가 POST라면 폼에서 받은 데이터를 PostForm으로.
        form = PostForm(request.POST)
        if form.is_valid():  # 받은 값들이 올바른지 확인.
            post = form.save(commit=False)  # 바로 저장하지 말고
            post.author = request.user  # 작성자 추가
            post.published_date = timezone.now()
            post.save()  # 변경사항 유지
            return redirect('post_detail', pk=post.pk)
            #redirect(to, permanent=False, *args, **kwargs)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    # blog/post_edit.html또 만들어야함
    # 템플릿에 전달할 데이터를 딕셔너리 형태로. 이때 value에 PostForm() 함수 호출하여 그 반환값을 넘기는 것.


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
