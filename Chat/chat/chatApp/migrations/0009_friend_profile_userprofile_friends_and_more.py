# Generated by Django 4.1 on 2022-08-22 15:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0008_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatApp.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='users_friends', to='chatApp.friend'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='blankprofilephoto.jpeg', null=True, upload_to='profile_images'),
        ),
    ]