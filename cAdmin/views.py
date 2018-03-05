from hashlib import md5
import urllib.request
from random import choice

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
    try:
        temporary_password = request.session['temp_password']
        del request.session['temp_password']
    except KeyError:
        temporary_password = ''

    user_list = User.objects.all()
    context = {
        'users': user_list,
        'temporary_password': temporary_password,
    }
    return render(request, 'admin/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request):
    """
    View to handle the deletion of users
    """
    user = User.objects.get(pk=int(request.POST['user']))
    user.delete()

    return HttpResponseRedirect(reverse('cAdmin:users'))


@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    """
    View to handle the creation of user
    """
    temporary_password = ''.join(choice('0123456789ABCDEF') for i in range(8))
    user = User.objects.create_user(
        username=request.POST['username'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=temporary_password,
    )

    encoded_email = request.POST['email'].encode('utf-8')

    gravatar_url = (
        'https://www.gravatar.com/avatar/' +
        md5(encoded_email.strip().lower()).hexdigest()
    )

    try:
        urllib.request.urlopen(gravatar_url+'?d=404')
        user.profile.gravatar_url = gravatar_url+'?s=1000'
        user.profile.gravatar_enabled = True
    except urllib.error.HTTPError:
        user.profile.associated_image = 'accounts/images/default_avatar.png'
        user.profile.gravatar_enabled = False

    user.clean()
    user.save()

    request.session['temp_password'] = temporary_password

    return HttpResponseRedirect(reverse('cAdmin:users'))


def github(request):
    """
    GitHub Integration settings page
    """
    context = {}
    return render(request, 'admin/github.html', context)
