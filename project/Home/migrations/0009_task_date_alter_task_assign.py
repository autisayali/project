# Generated by Django 4.2.7 on 2023-12-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_task_assign'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='assign',
            field=models.CharField(max_length=30),
        ),
    ]
