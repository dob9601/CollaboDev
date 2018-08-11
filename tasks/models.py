from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import now
from django.contrib.auth.models import User


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
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                   blank=True, default=None, null=True)
    task_priority = models.IntegerField(validators=[MaxValueValidator(10),
                                                    MinValueValidator(1)],
                                        blank=False)
    task_open = models.BooleanField(default=True)
    task_size = models.IntegerField(validators=[MaxValueValidator(7),
                                                MinValueValidator(1)],
                                    blank=False)

    bump_date = models.DateTimeField(default=now)

    created_by = models.CharField(max_length=20, blank=False)
    publish_date = models.DateTimeField(default=now, blank=True)
    deadline_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.task_name


class Repository(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=159, blank=False)
