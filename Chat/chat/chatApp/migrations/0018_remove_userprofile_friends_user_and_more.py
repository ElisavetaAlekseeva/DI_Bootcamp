# Generated by Django 4.1 on 2022-08-28 10:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chatApp', '0017_alter_friend_profile_alter_userprofile_friends_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(blank=True, to='chatApp.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='chatApp.user'),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='chatApp.user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chatApp.user'),
        ),
    ]
