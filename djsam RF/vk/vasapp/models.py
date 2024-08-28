from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=32)
    address = models.CharField(max_length=12)
    fee = models.IntegerField()
