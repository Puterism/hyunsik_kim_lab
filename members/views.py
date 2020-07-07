from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Member, Position
from .forms import MemberForm
from professor.models import Profile


def members(request):
    lists = []
    positions = Position.objects.all()
    professor = Profile.objects.last()

    for position in positions:
        lists.append({'position': position, 'members': Member.objects.filter(position=position.id)})

    context = {
        'lists': lists,
        'professor': professor,
    }
    return render(request, 'members/index.html', context)


@login_required
def members_add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('members')
        else:
            context = {
                'form': form,
            }
            return render(request, 'members/add.html', context)

    else:
        form = MemberForm()

        context = {
            'form': form,
        }
        return render(request, 'members/add.html', context)


@login_required
def members_edit(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)

        if form.is_valid():
            form.save()
            return redirect('members')
        else:
            context = {
                'member': member,
                'form': form,
            }
            return render(request, 'members/edit.html', context)

    else:
        form = MemberForm(instance=member)

        context = {
            'member': member,
            'form': form,
        }

        return render(request, 'members/edit.html', context)


@login_required
def members_delete(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('members')
