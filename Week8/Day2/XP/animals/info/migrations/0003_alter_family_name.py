# Generated by Django 4.1 on 2022-08-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_animal_family_alter_animal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
