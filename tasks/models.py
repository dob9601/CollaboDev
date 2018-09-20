"""Models for tasks app."""

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import now
from django.contrib.auth.models import User


class Task(models.Model):
    """Model containing information regarding a task."""

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

    is_pinned = models.BooleanField(default=False)

    created_by = models.CharField(max_length=20, blank=False)
    publish_date = models.DateTimeField(default=now, blank=True)
    deadline_date = models.DateTimeField(default=now)


class Repository(models.Model):
    """Model for Git repositories."""

    name = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=159, blank=False)
