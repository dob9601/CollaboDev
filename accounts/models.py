from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from tasks.models import Task


class Profile(models.Model):
    """
    Extension of user model, added automatically upon user creation.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )

    associated_image = models.CharField(
        default='/accounts/images/default_avatar.png',
        max_length=1000
    )
    associated_background = models.CharField(
        default='/accounts/images/default_avatar.png',
        max_length=1000
    )
    gravatar_url = models.URLField(
        default='',
        max_length=1000,
        blank=True
    )
    gravatar_enabled = models.BooleanField(default=False)

    url = models.URLField(max_length=2000,
                          blank=True)
    biography = models.CharField(max_length=300, blank=True)
    tasks_completed = models.IntegerField(default=0)
    dark_mode = models.BooleanField(default=True)


# pylint: disable=unused-argument
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create profile model upon user creation
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save user profile on user save
    """
    instance.profile.save()
