"""
CollaboDev URL Configuration.

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
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ProgrammingError, OperationalError
from django.conf import settings
from django.conf.urls.static import static

from admin.views import first_time_setup
from . import views


handler404 = 'CollaboDev.views.error404'  # pylint: disable=invalid-name

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', include('tasks.urls'), name='tasks'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', include('admin.urls'), name='cAdmin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

try:
    from admin.models import Settings
    SETTINGS = Settings.objects.get(pk=1)
    if not SETTINGS.settings_initialised:
        urlpatterns = [
            path('', first_time_setup),
        ]
except ObjectDoesNotExist:
    SETTINGS = Settings.objects.create(pk=1)
    SETTINGS.save()

    urlpatterns = [
        path('', first_time_setup),
    ]
except (OperationalError, ProgrammingError):
    pass
