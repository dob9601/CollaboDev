# Generated by Django 2.0 on 2018-06-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180619_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='associated_image',
            field=models.ImageField(blank=True, upload_to='profile_avatars/'),
        ),
    ]