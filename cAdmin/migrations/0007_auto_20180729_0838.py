# Generated by Django 2.0 on 2018-07-29 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cAdmin', '0006_auto_20180729_0838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='github_organisation_ur',
            new_name='github_organisation_url',
        ),
    ]
