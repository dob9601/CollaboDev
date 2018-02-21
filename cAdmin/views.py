from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    """
    Front page of administrative app
    """
    context = {}
    return render(request, 'admin/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    """
    User management page of administrative app
    """

    user_list = User.objects.all()
    context = {
        'users': user_list,
    }
    return render(request, 'admin/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request):
    user = User.objects.get(pk=int(request.POST['user']))
    user.delete()

    return HttpResponseRedirect(reverse('cAdmin:users'))
