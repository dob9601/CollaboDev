from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


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
        'chosen_user': User.objects.get(username=user)
    }
    return render(request, 'accounts/profile.html', context)


# Remove disable ASAP.
# pylint: disable-msg=too-many-branches
@login_required
def settings(request):
    context = {
        'error_first_name': False,
        'error_last_name': False,
        'error_biography': False,
        'error_url': False,

        'error_old_pword': False,
        'error_pword_conf': False,

        'successful_changes': [],
    }

    if request.method == 'POST':
        user = request.user

        user_first_name = request.POST['first_name']
        user_last_name = request.POST['last_name']
        user_profile_biography = request.POST['profile_biography']
        user_profile_url = request.POST['profile_url']

        # Profile
        if user_first_name == '':
            context['error_first_name'] = True
        else:
            user.first_name = user_first_name
            context['successful_changes'].append('first name')

        if user_last_name == '':
            context['error_last_name'] = True
        else:
            user.last_name = user_last_name
            context['successful_changes'].append('last name')

        if len(user_profile_biography) > 300:
            context['error_biography'] = True
        else:
            user.profile.biography = user_profile_biography
            context['successful_changes'].append('biography')

        if '://' not in user_profile_url:
            user_profile_url = 'http://' + user_profile_url
        try:
            url_validate = URLValidator()
            url_validate(user_profile_url)

            user.profile.url = user_profile_url
            context['successful_changes'].append('last name')
        except ValidationError:
            context['error_url'] = True
        # End of profile

        # Account
        user_username = request.POST['username']
        user.username = user_username
        # End of account

        # Password
        user_old_pword = request.POST['old_pword']
        user_new_pword = request.POST['new_pword']
        user_new_pword_conf = request.POST['new_pword_conf']

        if user_old_pword != '' or user_new_pword != '':
            # Old password validation
            if not user.check_password(user_old_pword):
                context['error_old_pword'] = True

            # New password validation
            elif user_new_pword != user_new_pword_conf:
                context['error_pword_conf'] = True
            else:
                user.set_password(user_new_pword)
                update_session_auth_hash(request, user)
                context['successful_changes'].append('password')
        # End of password

        user.save()

        context['successful_changes'][0] = (context['successful_changes'][0]
                                            .title())

    return render(request, 'accounts/settings.html', context)
