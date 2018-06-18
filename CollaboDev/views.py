from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

def index(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],
                            password = request.POST['password'])    
        if user is not None:
            auth_login(request, user)
            return redirect('/tasks/')
        else:
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html', {})

def logout(request):
    auth_logout(request)
    return redirect('/')
