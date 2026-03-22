from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    address = models.TextField()
    dept = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()