from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import user_verification


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
        'errors': [],
        'successful_changes': [],
    }

    if request.method == 'POST':
        user = request.user

        user_first_name = request.POST['first_name']
        user_last_name = request.POST['last_name']
        user_profile_biography = request.POST['profile_biography']
        user_profile_url = request.POST['profile_url']

        profile_clean = user_verification.clean_profile_changes(
            user_first_name,
            user_last_name,
            user_profile_biography,
            user_profile_url,
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
