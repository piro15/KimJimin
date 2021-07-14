from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# 애플리케이션의 로직 넣는 곳. 모델에서 정보 받아오고 템플릿에 전달.


def post_new(request):
    if request.method == "POST":  # method가 POST라면 폼에서 받은 데이터를 PostForm으로.
        form = PostForm(request.POST)
        if form.is_valid():  # 받은 값들이 올바른지 확인.
            post = form.save(commit=False)  # 바로 저장하지 말고
            post.author = request.user  # 작성자 추가
            post.published_date = timezone.now()
            post.save()  # 변경사항 유지하고 이 차례에서 새 블로그 글 생성.
            return redirect('post_detail', pk=post.pk)
            # redirect(to, permanent=False, *args, **kwargs) post_detail 뷰로 가기. 어느 글인지 알려면 pk변수 필요하니까 이 값 갖고서.
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    # blog/post_edit.html또 만들어야함
    # 템플릿에 전달할 데이터를 딕셔너리 형태로. 이때 value에 PostForm() 함수 호출하여 그 반환값을 넘기는 것.


def post_list(request):
    posts = Post.objects.filter(  # 변수. 이 변수를 쿼리셋의 이름. 이 쿼리셋을 이제 밑에 줄에서 템플릿으로 보낸다.
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # 그냥 Post.objects.get(pk=pk)라고 하면, 오류나왔을 때 오류가 뜬다. 예외처리같은 느낌으로 이에 대비해 404 나오게 만드는 것.
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
