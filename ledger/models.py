from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=10)
    birth_date = models.DateField()
    hire_date = models.DateField()
    
