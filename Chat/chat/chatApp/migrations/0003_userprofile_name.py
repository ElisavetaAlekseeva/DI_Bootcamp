# Generated by Django 4.1 on 2022-09-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0002_remove_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]