# Generated by Django 4.2.7 on 2023-11-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_name_entry_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.CharField(default='Yes', max_length=10),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default='High', max_length=20),
        ),
    ]