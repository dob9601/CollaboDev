from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Task, Quest


@login_required
def index(request):
    tasks = Task.objects.order_by('-publish_date')
    
    context = {
        'tasks': tasks,
    }
    try:
        message_id = request.session['response_message']
        if message_id == 1:
            message = "Task claimed successfully."
        elif message_id == 2:
            message = "Task already claimed."
        elif message_id == 3:
            message = "POST data did not contain a task ID."
        elif message_id == 4:
            message = "Task created successfully."
        elif message_id == 5:
            message = "Please completely fill out the form."
        elif message_id == 6:
            message = "Task unclaimed successfully."
        elif message_id == 7:
            message = "Task closed successfully."
        context['error_message'] = message
        del request.session['response_message']
    except KeyError:
        pass

    return render(request, 'tasks/index.html', context)


@login_required
def delete(request):
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

@login_required
def quests(request):
    user = User.objects.get(id=request.user.id)
    quest = Quest.objects.get(id=1)
    quest_tasks = quest.quest_tasks
    quest_stage = quest.quest_stage
    current_task = quest_tasks.get(quest_position=quest_stage)
    
    context = {
        'quest_stage': quest_stage,
        'current_task': current_task,
    }
    return render(request, 'tasks/quests.html', context)
