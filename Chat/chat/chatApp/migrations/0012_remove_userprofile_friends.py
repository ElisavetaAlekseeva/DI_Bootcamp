# Generated by Django 4.1 on 2022-08-23 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0011_userprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
    ]
