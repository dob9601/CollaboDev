from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Task(models.Model):
    """
    Arguments:
        task_name: Name of task (max of 70 characters)
        task_description: Description of task (max of 400 characters)
        task_owner: Username of person assigned to task (max of 15 characters)
        task_priority: The priority of a task (integer between 1 and 10)
        publish_date: The date the task was published on
        deadline_date: The date the task should be completed by
    """

    task_name = models.CharField(max_length=70, blank=False)
    task_description = models.CharField(max_length=400)
    task_owner = models.CharField(max_length=15)
    task_priority = models.IntegerField(validators=[MaxValueValidator(10),
                                                    MinValueValidator(1)],
                                        blank=False)
    task_open = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=now, blank=True)
    deadline_date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.task_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


