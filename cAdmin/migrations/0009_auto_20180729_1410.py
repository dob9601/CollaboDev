# Generated by Django 2.0 on 2018-07-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cAdmin', '0008_settings_github_org_repos_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='github_organisation_name',
            new_name='github_org_name',
        ),
    ]