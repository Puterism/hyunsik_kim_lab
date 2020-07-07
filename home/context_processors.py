from .models import Site
from notice.models import Article


def add_variable_to_context(request):
    site = Site.objects.last()
    recent_notice = Article.objects.last()

    return {
        'site': site,
        'recent_notice': recent_notice,
    }
