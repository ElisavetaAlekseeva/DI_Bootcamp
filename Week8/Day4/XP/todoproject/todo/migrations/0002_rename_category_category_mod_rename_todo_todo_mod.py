# Generated by Django 4.1 on 2022-08-14 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category_mod',
        ),
        migrations.RenameModel(
            old_name='ToDO',
            new_name='ToDO_mod',
        ),
    ]
