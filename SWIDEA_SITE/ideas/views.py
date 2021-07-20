from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm


def idea_list(request):
    idea = Idea.objects.all()
    ctx = {'idea': idea}
    return render(request, template_name='list.html', context=ctx)


def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea': idea}
    return render(request, template_name='detail.html', context=ctx)


def create_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('ideas:idea_detail')
    else:
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, template_name='create.html', context=ctx)


def edit_idea(request):
    pass


def idea_delete(request, pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('ideas:idea_list')
