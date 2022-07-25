from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class TaskData(models.Model):
    empid = models.TextField(max_length=20)
    empname = models.TextField(max_length=50)
    empemail = models.TextField(max_length=50)
    taskname = models.TextField(max_length=100)
    duedate = models.TextField(max_length=20)
    taskstatus = models.TextField(max_length=15)
    tasksummary = models.TextField(max_length=500)

