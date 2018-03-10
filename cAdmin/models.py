from django.db import models


class Settings(models.Model):
    """
    Global settings for the whole CollaboDev WebApp.
    There should only be ONE INSTANCE of this model.
    """
    # GITHUB
    github_integrated = models.BooleanField(default=False)

    # PROFILE
    profile_allow_biography = models.BooleanField(default=True)
    profile_allow_name_changes = models.BooleanField(default=False)
    profile_allow_username_changes = models.BooleanField(default=False)

    profile_allow_change_requests = models.BooleanField(default=True)

    # USER
    users_show_completed_tasks = models.BooleanField(default=True)
    users_show_email = models.BooleanField(default=True)
    users_show_online = models.BooleanField(default=True)

    # TASKS
    tasks_show_xp_bar = models.BooleanField(default=True)

    # CONFIG
    settings_initialised = models.BooleanField(default=False)
    settings_setup_code = models.CharField(blank=True, max_length=19)
