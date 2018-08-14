"""Views for tasks app."""

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required

from .models import Task


@login_required
def index(request):
    """View for the tasks list."""
    tasks = list(Task.objects.order_by('-bump_date'))

    moved_tasks = 0
    for task in tasks:
        if task.task_owner == request.user:
            tasks.remove(task)
            tasks.insert(moved_tasks, task)
            moved_tasks += 1

    context = {
        'tasks': tasks,
    }
    try:
        message_id = request.session['response_message']
        if message_id == 1:
            message = 'Task claimed successfully.'
        elif message_id == 2:
            message = 'Task already claimed.'
        elif message_id == 3:
            message = 'POST data did not contain a task ID.'
        elif message_id == 4:
            message = 'Task created successfully.'
        elif message_id == 5:
            message = 'Please completely fill out the form.'
        elif message_id == 6:
            message = 'Task unclaimed successfully.'
        elif message_id == 7:
            message = 'Task closed successfully.'
        elif message_id == 8:
            message = 'You are already on a task'
        context['error_message'] = message
        del request.session['response_message']
    except KeyError:
        pass

    return render(request, 'tasks/index.html', context)


@login_required
def milestones(request):
    """Temporary placeholder for milestones page."""
    return render(request, 'tasks/milestones.html', {})


@login_required
def delete(request):
    """
    Temporary view to facilitate the removal of tasks.

    To be removed as soon as viable alternative available.
    """
    try:
        task_id = request.POST['id']
        Task.objects.get(pk=int(task_id)).delete()
        return HttpResponse('Task deleted.')

    except MultiValueDictKeyError:
        tasks = Task.objects.order_by('-publish_date')
        context = {
            'tasks': tasks,
        }
        return render(request, 'tasks/delete.html', context)
