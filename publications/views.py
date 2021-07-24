from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
import json

from .models import Description, Publication
from .forms import DescriptionForm, PublicationForm


def publications(request):
    publications_list = Publication.objects.filter(
        created_at__lte=timezone.now()).order_by('-order')
    description = Description.objects.last()

    context = {
        'publications': publications_list,
        'description': description,
    }
    return render(request, 'publications/index.html', context)


@login_required
def publications_add(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('publications')
        else:
            context = {
                'message': '에러가 발생했습니다'
            }
            return render(request, 'publications/add.html', context)
            # return redirect('publication_add')

    else:
        form = PublicationForm()
        context = {
            'form': form,
        }
        return render(request, 'publications/add.html', context)


@login_required
def publications_edit(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)

        if form.is_valid():
            form.save()
            return redirect('publications')
        else:
            context = {
                'message': '에러가 발생했습니다'
            }
            return render(request, 'publications/edit.html', context)

    else:
        form = PublicationForm(instance=publication)
        context = {
            'publication': publication,
            'form': form,
        }
        return render(request, 'publications/edit.html', context)


@login_required
def publications_delete(request, id):
    publication = get_object_or_404(Publication, id=id)
    publication.delete()
    return redirect('publications')


@login_required
def publications_edit_order(request):
    publications_list = Publication.objects.filter(
        created_at__lte=timezone.now()).order_by('-order')

    if request.method == 'POST':
        try:
            unicode = request.body.decode('utf-8')
            data = json.loads(unicode)

            for id in data:
                order = data[id]['order']
                publication = Publication.objects.get(id=id)
                if publication.order != order:
                    publication.order = order
                    publication.save(update=True)

        except Exception:
            return JsonResponse({
                'status': 'failure',
                'message': '서버 문제로 저장하지 못했습니다. 잠시 후 다시 시도해주세요.',
            }, status=500)

        return JsonResponse({'status': 'success'})
    else:
        context = {
            'publications': publications_list,
        }

        return render(request, 'publications/edit_order.html', context)


@login_required
def publications_description_edit(request):
    description = Description.objects.last()

    if request.method == 'POST':
        form = DescriptionForm(request.POST, instance=description)

        if form.is_valid():
            form.save()
            return redirect('publications')
        else:
            context = {
                'message': '에러가 발생했습니다'
            }
            return render(request, 'publications/description_edit.html', context)

    else:
        form = DescriptionForm(instance=description)
        context = {
            'description': description,
            'form': form,
        }
        return render(request, 'publications/description_edit.html', context)
