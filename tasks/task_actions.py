from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

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
        )
        new_task.clean()
        new_task.save()

        return HttpResponseRedirect(reverse('tasks:index') + "?m=4")
    except ValidationError:
        return HttpResponseRedirect(reverse('tasks:index') + "?m=5")


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
            return HttpResponseRedirect(reverse('tasks:index') + "?m=1")
        else:
            return HttpResponseRedirect(reverse('tasks:index') + "?m=2")
            # return HttpResponse('Task already claimed.')
            # return task already claimed
            # read logged in user
            # assign chosen task to user
    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('tasks:index') + "?m=3")


@login_required
def unclaim(request):
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.task_owner = ""
        chosen_task.save()
        return HttpResponseRedirect(reverse('tasks:index') + "?m=6")

    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('tasks:index') + "?m=3")


@login_required
def close(request):
    try:
        task_id = request.POST['task_id']
        chosen_task = Task.objects.get(pk=int(task_id))
        chosen_task.task_open = False
        chosen_task.save()
        return HttpResponseRedirect(reverse('tasks:index') + "?m=7")

    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('tasks:index') + "?m=3")
