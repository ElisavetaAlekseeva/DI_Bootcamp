# Generated by Django 4.1 on 2022-08-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0007_userprofile_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
