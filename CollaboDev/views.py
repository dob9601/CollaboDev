"""Views for CollaboDev WebApp."""

import random
import os

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.http import HttpResponseNotFound
from .settings import BASE_DIR


def index(request):
    """View for front page of CollaboDev WebApp."""
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/tasks/')
        return render(request, 'index.html', {})
    return render(request, 'index.html', {})


def logout(request):
    """Logout view of CollaboDev WebApp."""
    auth_logout(request)
    return redirect('/')


def error404(request, exception):
    """View for 404 page."""
    responses = open(os.path.join(BASE_DIR, 'CollaboDev/404_responses.txt'))
    responses = responses.read().split('\n')

    message = random.choice(responses)
    context = {
        'message': message,
        'error': exception
    }

    return HttpResponseNotFound(render(request, '404.html', context))
