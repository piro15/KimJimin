from django.shortcuts import get_object_or_404, render, redirect
from .models import Idea
from .forms import IdeaForm


def idea_list(request):
    idea = Idea.objects.all()
    ctx = {'idea': idea}
    return render(request, template_name='idea/list.html', context=ctx)


def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea': idea}
    return render(request, template_name='idea/detail.html', context=ctx)


def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('ideas:idea_detail')
    else:
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, template_name='idea/form.html', context=ctx)


def idea_edit(request, pk):
    post = get_object_or_404(Idea, id=pk)
    if request.method == 'POST':
        idea = IdeaForm(request.POST, instance=post)
        if idea.is_valid():
            post = idea.save()
            return redirect('tools:tool_detail', pk)
    else:
        idea = IdeaForm(instance=post)
        ctx = {'idea': idea}
        return render(request, template_name='idea/form.html', context=ctx)


def idea_delete(pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('ideas:idea_list')
