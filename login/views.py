from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, logout as django_logout, authenticate


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            django_login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login/login.html')


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')