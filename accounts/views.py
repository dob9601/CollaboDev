from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


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


@login_required
def settings(request):
    context = {
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

        user_username = request.POST['username']
    
        user_old_pword = request.POST['old_pword']
        user_new_pword = request.POST['new_pword']
        user_new_pword_conf = request.POST['new_pword_conf']


        if user_old_pword != '' or user_new_pword != '':
            # Old password validation
            if not user.check_password(user_old_pword):
                context['error_old_pword'] = True
    
            # New password validation
            if user_new_pword != user_new_pword_conf:
                context['error_pword_conf'] = True
            if not context['error_pword_conf'] and not context['error_old_pword']:
                user.set_password(user_new_pword)
                user.save()
                update_session_auth_hash(request, user)
                context['successful_changes'].append('password')

        
        context['successful_changes'][0] = context['successful_changes'][0].title()

    return render(request, 'accounts/settings.html', context)
