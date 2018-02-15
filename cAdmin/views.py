from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    """
    Front page of administrative app
    """
    context = {}
    return render(request, 'admin/index.html', context)


def users(request):
    """
    User management page of administrative app
    """

    user_list = User.objects.all()
    context = {
        'users': user_list,
    }
    return render(request, 'admin/users.html', context)
