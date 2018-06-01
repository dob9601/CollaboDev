from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('user_status/', views.user_status, name='user_status'),
    path('<str:user>/', views.profile, name='profile'),
]
