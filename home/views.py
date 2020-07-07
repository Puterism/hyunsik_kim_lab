from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HomeForm, SiteForm
from .models import Home, Site
from members.models import Member
from notice.models import Article


def index(request):
    home = Home.objects.last()
    members = Member.objects.all().order_by('-updated_at')
    # articles = Article.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:2]
    article = Article.objects.last()

    context = {
        'home': home,
        'members': members,
        'article': article,
    }
    return render(request, 'home/index.html', context)


@login_required
def home_edit(request):
    home = Home.objects.last()

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=home)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'home': home,
                'form': form,
            }
            return render(request, 'home/edit.html', context)

    else:
        form = HomeForm(instance=home)
        context = {
            'home': home,
            'form': form
        }

        return render(request, 'home/edit.html', context)


@login_required
def site_setting(request):
    site = Site.objects.last()

    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES, instance=site)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'site': site,
                'form': form,
            }
            return render(request, 'home/site_setting.html', context)

    else:
        form = SiteForm(instance=site)
        context = {
            'site': site,
            'form': form
        }

        return render(request, 'home/site_setting.html', context)
