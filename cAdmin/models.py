from django.db import models


class Settings(models.Model):
    # GitHub settings
    github_integrated = models.BooleanField(default=False)

    # Profile settings
    profile_allow_biography = models.BooleanField(default=True)
    profile_allow_name_changes = models.BooleanField(default=False)
    profile_allow_username_changes = models.BooleanField(default=False)

    profile_allow_change_requests = models.BooleanField(default=True)

    # User settings
    users_show_completed_tasks = models.BooleanField(default=True)
    users_show_email = models.BooleanField(default=True)
    users_show_online = models.BooleanField(default=True)

    # Tasks settings
    tasks_show_xp_bar = models.BooleanField(default=True)
