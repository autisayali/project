# Generated by Django 4.2.7 on 2023-11-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.CharField(max_length=10),
        ),
    ]
