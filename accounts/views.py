from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


def profile(request, user):
    context = {
        'chosen_user': User.objects.get(username=user)
    }
    return render(request, 'accounts/profile.html', context)


def settings(request):
    context = {}
    return render(request, 'accounts/settings.html', context)
