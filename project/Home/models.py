from django.db import models


# Create your models here.
class Entry(models.Model):
    uname=models.CharField(max_length=10,primary_key=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=5)
    
from Home.models import Entry
class Task(models.Model):
    id=models.IntegerField(primary_key=True)
    taskdate=models.CharField(max_length=20)
    desc=models.CharField(max_length=50)
    priority=models.CharField(max_length=20)
    complete=models.CharField(max_length=10)
    assign=models.CharField(max_length=30)
   
    
