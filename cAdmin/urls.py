from django.urls import path

from . import views

app_name = 'cAdmin'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users/delete/', views.delete_user, name='delete_user'),
    path('users/create/', views.create_user, name='create_user'),
]
