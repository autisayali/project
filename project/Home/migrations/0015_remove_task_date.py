# Generated by Django 4.2.7 on 2023-12-01 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_alter_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]