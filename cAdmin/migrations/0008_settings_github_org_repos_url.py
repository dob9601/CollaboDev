# Generated by Django 2.0 on 2018-07-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cAdmin', '0007_auto_20180729_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='github_org_repos_url',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]
