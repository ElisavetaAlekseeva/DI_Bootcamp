# Generated by Django 4.1 on 2022-08-14 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_category_category_mod_rename_todo_todo_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_mod',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todo.category_mod'),
        ),
    ]
