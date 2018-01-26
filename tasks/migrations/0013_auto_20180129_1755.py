# Generated by Django 2.0 on 2018-01-29 17:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0012_profile_current_quest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_name', models.CharField(max_length=70)),
                ('quest_description', models.CharField(max_length=400)),
                ('quest_priority', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('quest_open', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('deadline_date', models.DateTimeField()),
                ('quest_owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('quest_tasks', models.ManyToManyField(to='tasks.Task')),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='current_quest',
            new_name='quest',
        ),
    ]
