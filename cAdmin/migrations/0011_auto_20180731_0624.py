# Generated by Django 2.0 on 2018-07-31 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cAdmin', '0010_auto_20180729_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='github_org_url',
            new_name='github_org_api_url',
        ),
    ]
