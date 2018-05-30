"""CollaboDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ProgrammingError, OperationalError

from cAdmin.views import first_time_setup

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('tasks/', include('tasks.urls'), name='tasks'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', include('cAdmin.urls'), name='cAdmin'),
]

try:
    from cAdmin.models import Settings
    settings = Settings.objects.get(id=1)
    if not settings.settings_initialised:
        urlpatterns = [
            path('', first_time_setup),
        ]
except ObjectDoesNotExist:
    settings = Settings.objects.create(id=1)
    settings.save()

    urlpatterns = [
        path('', first_time_setup),
    ]
except (OperationalError, ProgrammingError):
    pass
