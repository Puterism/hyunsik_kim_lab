from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, MenuForm, ItemForm
from .models import Profile, Menu, Item


def get_professor_profile():
    profile = Profile.objects.filter(id=1)
    return profile[0]


def get_professor_lists():
    menus = Menu.objects.all()
    lists = []

    for menu in menus:
        lists.append({
            'id': menu.id,
            'header': menu.header,
            'items': Item.objects.filter(menu=menu.id).order_by('-year')
        })

    return lists


def professor(request):
    profile = get_professor_profile()
    lists = get_professor_lists()

    context = {
        'profile': profile,
        'lists': lists,
    }

    return render(request, 'professor/index.html', context)


@login_required
def professor_profile_edit(request):
    profile = get_professor_profile()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('professor')
        else:
            context = {
                'profile': profile,
                'form': form,
            }
            return render(request, 'professor/profile_edit.html', context)

    else:
        form = ProfileForm(instance=profile)
        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'professor/profile_edit.html', context)


@login_required
def professor_menu_add(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('professor')
        else:
            context = {
                'form': form,
            }
            return render(request, 'professor/menu_add.html', context)

    else:
        form = MenuForm()
        context = {
            'form': form,
        }
        return render(request, 'professor/menu_add.html', context)


@login_required
def professor_menu_edit(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)

        if form.is_valid():
            form.save()
            return redirect('professor')
        else:
            context = {
                'form': form,
                'menu': menu,
            }
            return render(request, 'professor/menu_edit.html', context)

    else:
        form = MenuForm(instance=menu)
        context = {
            'form': form,
            'menu': menu,
        }
        return render(request, 'professor/menu_edit.html', context)


@login_required
def professor_menu_delete(request, id):
    menu = get_object_or_404(Menu, id=id)
    menu.delete()
    return redirect('professor')


@login_required
def professor_item_add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('professor')
        else:
            context = {
                'form': form,
            }
            return render(request, 'professor/item_add.html', context)

    else:
        form = ItemForm()
        context = {
            'form': form,
        }
        return render(request, 'professor/item_add.html', context)


@login_required
def professor_item_edit(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('professor')
        else:
            context = {
                'form': form,
                'item': item,
            }
            return render(request, 'professor/item_edit.html', context)

    else:
        form = ItemForm(instance=item)
        context = {
            'form': form,
            'item': item,
        }
        return render(request, 'professor/item_edit.html', context)


@login_required
def professor_item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('professor')
