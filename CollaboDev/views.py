from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate


def index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/tasks/')
        return render(request, 'index.html', {})
    return render(request, 'index.html', {})


def logout(request):
    auth_logout(request)
    return redirect('/')
