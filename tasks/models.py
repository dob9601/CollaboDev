from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import now

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
