from django.shortcuts import get_object_or_404, render, redirect
from .models import Tool
from .forms import ToolForm

# Create your views here.


def tool_list(request):
    tool = Tool.objects.all()
    ctx = {'tool': tool}
    return render(request, template_name='devtool/list.html', context=ctx)


def tool_detail(request, pk):
    tool = Tool.objects.get(id=pk)
    ctx = {'tool': tool}
    return render(request, template_name='devtool/detail.html', context=ctx)


def tool_create(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('devtools:tool_list', pk=post.pk)
    else:
        form = ToolForm()
        ctx = {'form': form}
        return render(request, template_name='devtool/form.html', context=ctx)


def tool_edit(request, pk):
    post = get_object_or_404(Tool, id=pk)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('devtools:tool_detail', pk)
    else:
        form = ToolForm(instance=post)
        ctx = {'form': form}
        return render(request, template_name='devtool/form.html', context=ctx)


def tool_delete(request, pk):
    tool = Tool.objects.get(id=pk)
    tool.delete()
    return redirect('devtools:tool_list')
