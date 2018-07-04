from datetime import timedelta
from json import dumps

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from . import user_verification


@login_required
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


@login_required
def profile(request, user):
    context = {
        'chosen_user': User.objects.get(username=user),
    }

    time_difference = timezone.now() - context['chosen_user'].profile.last_ping
    context['chosen_user_online'] = bool(time_difference < timedelta(0, 70))

    return render(request, 'accounts/profile.html', context)


@login_required
def user_status(request):
    data = request.body.decode('utf-8').split('@')

    if data[0] == 'U':
        session = Session.objects.get(session_key=data[1])
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=user_id)

        user.profile.last_ping = timezone.now()
        user.save()

        payload = {'success': True}

    elif data[0] == 'R':
        user = User.objects.get(pk=data[1])

        time_difference = timezone.now() - user.profile.last_ping
        status = bool(time_difference < timedelta(0, 40))

        payload = {'success': True, 'status': status}

    else:
        payload = {'success': False}

    return HttpResponse(dumps(payload), content_type='application/json')


# Remove disable ASAP.
# pylint: disable-msg=too-many-branches, too-many-locals, duplicate-code
@login_required
def settings(request):
    context = {
        'errors': [],
        'successful_changes': [],
    }

    if request.method == 'POST':
        user = request.user

        user_first_name = request.POST.get('first_name', '')
        user_last_name = request.POST.get('last_name', '')
        user_profile_biography = request.POST.get('profile_biography', '')
        user_profile_url = request.POST.get('profile_url', '')

        background = request.FILES.get('background', False)
        avatar = request.FILES.get('avatar', False)

        reset_background = request.POST.get('reset_background', False)
        reset_avatar = request.POST.get('reset_avatar', False)
        gravatar_enabled = request.POST.get('gravatar_enabled', False)

        profile_clean = user_verification.clean_profile_changes(
            user_first_name,
            user_last_name,
            user_profile_biography,
            user_profile_url,
            reset_background,
            background,
            reset_avatar,
            avatar,
            gravatar_enabled,
            user
        )
        user = profile_clean[0]
        context['successful_changes'] += profile_clean[1]
        context['errors'] += profile_clean[2]

        # Account
        user_username = request.POST['username']
        user.username = user_username
        # End of account

        user_old_pword = request.POST['old_pword']
        user_new_pword = request.POST['new_pword']
        user_new_pword_conf = request.POST['new_pword_conf']

        password_clean = user_verification.clean_password_changes(
            user_old_pword,
            user_new_pword,
            user_new_pword_conf,
            user,
            request
        )
        user = password_clean[0]
        context['successful_changes'] += password_clean[1]
        context['errors'] += password_clean[2]

        user.save()

    return render(request, 'accounts/settings.html', context)
