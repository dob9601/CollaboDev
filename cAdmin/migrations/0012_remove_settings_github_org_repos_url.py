# Generated by Django 2.0 on 2018-07-31 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cAdmin', '0011_auto_20180731_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='github_org_repos_url',
        ),
    ]
