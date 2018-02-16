from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Task(models.Model):
    """
    A model containing information regarding a piece of work that needs to be
    done.

    Arguments:
        task_name: Name of task (max of 70 characters)
        task_description: Description of task (max of 400 characters)
        task_owner: Username of person assigned to task (max of 15 characters)
        task_priority: The priority of a task (integer between 1 and 10)
        created_by: The username of the user that created the task
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
    task_size = models.IntegerField(validators=[MaxValueValidator(7),
                                                MinValueValidator(1)],
                                    blank=False)

    quest_position = models.IntegerField(default=-1)

    created_by = models.CharField(max_length=20, blank=False)
    publish_date = models.DateTimeField(default=now, blank=True)
    deadline_date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.task_name


class Profile(models.Model):
    """
    Extension of user model, added automatically upon user creation.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField(default=0)
    associated_image = models.CharField(
        default='/accounts/images/default_avatar.png',
        max_length=1000
    )
    quest = models.CharField(default='null', max_length=1000)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create profile model upon user creation
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Quest(models.Model):
    """
    A series of tasks interlinked as part of 1 large quest.
    """
    quest_name = models.CharField(max_length=70, blank=False)
    quest_description = models.CharField(max_length=400)
    quest_owner = models.ManyToManyField(User)
    quest_priority = models.IntegerField(validators=[MaxValueValidator(10),
                                                     MinValueValidator(1)],
                                         blank=False)
    quest_open = models.BooleanField(default=True)
    quest_tasks = models.ManyToManyField(Task)
    quest_stage = models.IntegerField(default=0)

    publish_date = models.DateTimeField(default=now, blank=True)
    deadline_date = models.DateTimeField(blank=False)
