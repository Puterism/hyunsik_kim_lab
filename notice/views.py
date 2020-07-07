from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    number = paged_articles.number
    num_pages = paged_articles.paginator.num_pages
    start = number - 3 if number >= 3 else 0
    end = number + 2 if number <= num_pages - 2 else num_pages
    paginator_range = list(paginator.page_range)[start:end]

    context = {
        'articles': paged_articles,
        'paginator_range': paginator_range,
    }
    return render(request, 'notice/article_list.html', context)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'notice/article_view.html', context)


@login_required
def article_write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('article_list')
        else:
            return redirect('article_write')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'notice/article_write.html', context)


@login_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('article_view', id)
        else:
            return redirect('article_list')

    else:
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'notice/article_edit.html', context)


@login_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('article_list')
