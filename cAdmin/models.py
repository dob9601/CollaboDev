from django.db import models


class Settings(models.Model):
    """
    Global settings for the whole CollaboDev WebApp.
    There should only be ONE INSTANCE of this model.
    """
    # GITHUB
    github_org_name = models.CharField(max_length=39, blank=True)
    github_org_url = models.URLField(max_length=2000, blank=True)
    github_org_api_url = models.URLField(max_length=2000, blank=True)

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
    
    def save(self, *args, **kwargs):
        if self.github_org_name:
            self.github_org_url = 'https://github.com/orgs/' + self.github_org_name
            self.github_org_api_url = 'https://api.github.com/orgs/' + self.github_org_name
        super(Settings, self).save(*args, **kwargs)
