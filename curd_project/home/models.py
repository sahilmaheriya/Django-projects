from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 122)
    email = models.EmailField(max_length =122)
    phone = models.IntegerField(max_length=12)
    