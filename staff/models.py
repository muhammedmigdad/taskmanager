from django.db import models
from django.contrib.auth.models import User
from staff.models import *



class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "staff"
        verbose_name = "staff"
        verbose_name_plural = "staffs"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email
    
    
    
class Task(models.Model):
    task = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'web_task'
        verbose_name = ('task')
        verbose_name_plural = ('tasks')
        ordering = ['-id']

    def _str_(self):
        return self.task





