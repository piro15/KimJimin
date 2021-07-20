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
            tool = form.save()
            return redirect('tools:tool_detail')
    else:
        form = ToolForm()
        ctx = {'form': form}
        return render(request, template_name='devtool/form.html', context=ctx)


def tool_edit(request, pk):
    post = get_object_or_404(Tool, id=pk)
    if request.method == 'POST':
        tool = ToolForm(request.POST, instance=post)
        if tool.is_valid():
            post = tool.save()
            return redirect('tools:tool_detail', pk)
    else:
        tool = ToolForm(instance=post)
        ctx = {'tool': tool}
        return render(request, template_name='devtool/form.html', context=ctx)


def tool_delete(pk):
    tool = Tool.objects.get(id=pk)
    tool.delete()
    return redirect('tools:tool_list')
