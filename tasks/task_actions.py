"""Module containing views for task manipulation."""

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Task


@login_required
def submit(request):
    """
    View that handles the submission of task data.

    Works by parsing all data from the request for the task and raising an
    error if any of the required data is missing.
    """
    if request.POST['task_owner'] != '':
        task_owner = User.objects.get(username=request.POST['task_owner'])
    else:
        task_owner = None

    try:
        new_task = Task(
            task_name=request.POST['task_name'],
            task_description=request.POST['task_description'],
            task_owner=task_owner,
            task_priority=request.POST['task_priority'],
            task_size=request.POST['task_size'],
        )
        if request.POST['deadline_date'] != '':
            new_task.deadline_date = request.POST['deadline_date']

        new_task.clean()
        new_task.save()

        request.session['response_message'] = 4
        return HttpResponseRedirect(reverse('tasks:index'))
    except ValidationError:
        request.session['response_message'] = 5
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def claim(request):
    """View that handles the claiming of new tasks."""
    try:
        task_id = request.POST['task_id']
        new_owner = request.user
        task = Task.objects.get(pk=int(task_id))
        old_owner = task.task_owner

        if old_owner is None:
            try:
                previous_task = request.user.profile.current_task
                previous_task.task_owner = None
                previous_task.save()
            except AttributeError:
                pass

            task.task_owner = new_owner
            task.save()
            request.session['response_message'] = 1

            request.user.profile.current_task = task
            request.user.save()

            return HttpResponseRedirect(reverse('tasks:index'))

        request.session['response_message'] = 2
        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def unclaim(request):
    """View that handles the pressing of the 'unclaim task' button."""
    try:
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=int(task_id))
        task.task_owner = None
        task.save()

        user = request.user
        user.profile.current_task = None
        user.save()

        request.session['response_message'] = 6
        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def close(request):
    """View that handles the closing/completion of tasks."""
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.task_open = False
        chosen_task.task_owner = None
        chosen_task.save()

        user = request.user
        user.profile.current_task = None
        user.profile.tasks_completed += chosen_task.task_size
        user.save()

        request.session['response_message'] = 7
        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))


@user_passes_test(lambda u: u.is_superuser)
def pin_task(request):
    """View that handles the pinning/unpinning of tasks."""
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.is_pinned = not chosen_task.is_pinned
        chosen_task.save()

        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))
