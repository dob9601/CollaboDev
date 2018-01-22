from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Task


@login_required
def create(request):
    return render(request, 'tasks/create.html', {})


@login_required
def submit(request):
    try:
        new_task = Task(
            task_name=request.POST['task_name'],
            task_description=request.POST['task_description'],
            task_owner=request.POST['task_owner'],
            task_priority=request.POST['task_priority'],
            deadline_date=request.POST['deadline_date'],
            task_size=request.POST['task_size'],
        )
        new_task.clean()
        new_task.save()
        
        request.session['response_message'] = 4
        return HttpResponseRedirect(reverse('tasks:index'))
    except ValidationError:
        request.session['response_message'] = 5
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def claim(request):
    try:
        task_id = request.POST['task_id']
        new_owner = "dob9601"  # Change to read from user db and logged in user
        chosen_task = Task.objects.get(pk=int(task_id))
        old_owner = chosen_task.task_owner

        if old_owner == "":
            chosen_task.task_owner = new_owner
            chosen_task.save()
            request.session['response_message'] = 1
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            request.session['response_message'] = 2
            return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def unclaim(request):
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.task_owner = ""
        chosen_task.save()
        request.session['response_message'] = 6
        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def close(request):
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.task_open = False
        chosen_task.save()
        
        current_user = request.user.id
        user = User.objects.get(id=current_user)
        user.profile.tasks_completed += chosen_task.task_size
        user.save()

        request.session['response_message'] = 7
        return HttpResponseRedirect(reverse('tasks:index'))

    except MultiValueDictKeyError:
        request.session['response_message'] = 3
        return HttpResponseRedirect(reverse('tasks:index'))
