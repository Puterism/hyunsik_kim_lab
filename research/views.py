from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.utils import timezone

from .models import Research
from .forms import ResearchForm


def research_list(request):
    research = Research.objects.filter(created_at__lte=timezone.now()).order_by('-year')

    context = {
        'research': research
    }

    return render(request, 'research/index.html', context)


@login_required
def research_add(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('research_list')
        else:
            context = {
                'message': '에러가 발생했습니다',
                'form': form,
            }
            return render(request, 'research/add.html', context)
    else:
        form = ResearchForm()
        context = {
            'form': form,
        }
        return render(request, 'research/add.html', context)


@login_required
def research_edit(request, order):
    research = get_object_or_404(Research, order=order)
    if request.method == 'POST':
        form = ResearchForm(request.POST, instance=research)

        if form.is_valid():
            form.save()
            return redirect('research_list')
        else:
            context = {
                'message': '에러가 발생했습니다',
                'research': research,
                'form': form,
            }
            return render(request, 'research/edit.html', context)

    else:
        form = ResearchForm(instance=research)
        context = {
            'research': research,
            'form': form,
        }
        return render(request, 'research/edit.html', context)


@login_required
def research_delete(request, order):
    research = get_object_or_404(Research, order=order)
    research.delete()
    return redirect('research_list')