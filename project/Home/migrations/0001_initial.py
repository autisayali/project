# Generated by Django 4.2.7 on 2023-11-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=5)),
                ('taskdate', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]
