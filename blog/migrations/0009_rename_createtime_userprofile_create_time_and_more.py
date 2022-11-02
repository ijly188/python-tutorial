# Generated by Django 4.1.1 on 2022-11-01 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='createtime',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='updatetime',
            new_name='update_time',
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('last_edit_update', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
