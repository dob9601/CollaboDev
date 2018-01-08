from django.urls import path

from . import views
from . import task_actions

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', task_actions.create, name='create'),
    path('submit/', task_actions.submit, name='submit'),
    path('delete/', views.delete, name='delete'),
    path('claim/', task_actions.claim, name='claim'),
    path('unclaim/', task_actions.unclaim, name='unclaim'),
    path('close/', task_actions.close, name='close')
]
