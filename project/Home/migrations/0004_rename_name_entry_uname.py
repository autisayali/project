# Generated by Django 4.2.7 on 2023-11-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_task_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='name',
            new_name='uname',
        ),
    ]
