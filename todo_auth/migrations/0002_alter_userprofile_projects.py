# Generated by Django 4.1 on 2022-10-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0002_remove_project_creator_remove_task_creator_and_more'),
        ('todo_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='projects',
            field=models.ManyToManyField(to='project_management.project'),
        ),
    ]
