from random import choice
from os import system

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Settings

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

    user.clean()
    user.save()

    request.session['temp_password'] = temporary_password

    return HttpResponseRedirect(reverse('cAdmin:users'))


@user_passes_test(lambda u: u.is_superuser)
def reset_collabodev():
    settings = Settings.objects.get(pk=1)
    settings.settings_initialised = False

    system('python manage.py flush --noinput')

    return HttpResponseRedirect(reverse('cAdmin:reset_page'))


def reset_page(request):
    try:
        Settings.objects.get(pk=1)
        context = {
            'derail': True
        }
    except ObjectDoesNotExist:
        context = {}

    return render(request, 'admin/reset_page.html', context)


@user_passes_test(lambda u: u.is_superuser)
def github(request):
    """
    GitHub Integration settings page
    """
    context = {}

    return render(request, 'admin/github.html', context)


def first_time_setup(request):
    """
    First time setup for when the software is first installed on a server
    """

    settings = Settings.objects.get(pk=1)

    context = {
        'password_page': True,
    }

    if request.method == 'POST':
        if 'setup-key' in request.POST:
            if request.POST['setup-key'] == settings.settings_setup_code:
                context['password_page'] = False
                context['settings'] = settings
        else:
            context = {}
            admin_pwd = request.POST['admin-password']
            admin_pwd_conf = request.POST['admin-password-conf']
            if admin_pwd == admin_pwd_conf:
                admin_user = User.objects.create_user(
                    username=request.POST['admin-username'],
                    first_name=request.POST['admin-first-name'],
                    last_name=request.POST['admin-last-name'],
                    email=request.POST['admin-email'],
                    password=admin_pwd
                )
                admin_user.is_superuser = True
                admin_user.save()
            else:
                pass
                # Raise password error

            if context == {}:
                settings.settings_initialised = True
                settings.save()
                context = {
                    'setup_complete': True
                }

    else:

        try:
            open("setup-key.txt", "r")
            if settings.settings_setup_code == "":
                raise FileNotFoundError
        except FileNotFoundError:
            key = ((''.join(choice('0123456789ABCDEF') for i in range(4))) +
                   '-' +
                   (''.join(choice('0123456789ABCDEF') for i in range(4))) +
                   '-' +
                   (''.join(choice('0123456789ABCDEF') for i in range(4))) +
                   '-' +
                   (''.join(choice('0123456789ABCDEF') for i in range(4))))

            key_string = "CollaboDev Setup Code: " + key

            with open("setup-key.txt", "w") as key_file:
                key_file.write(key_string)

            settings.settings_setup_code = key
            settings.save()

    return render(request, 'admin/first-time-setup.html', context)
