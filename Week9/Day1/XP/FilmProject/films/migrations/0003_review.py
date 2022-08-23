# Generated by Django 4.1 on 2022-08-18 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_address_alter_userprofile_hobbies_and_more'),
        ('films', '0002_film_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500, null=True)),
                ('rate', models.IntegerField(default=0, null=True)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]