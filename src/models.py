from django.db import models

# Create your models here.
class employeeRegistratoin(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.first_name

class employeeDetail(models.Model):
    employeeName=models.CharField(max_length=100)
    employeeDob=models.DateField(max_length=100)
    employeeEmail=models.EmailField(max_length=100)
    employeePhone=models.CharField(max_length=100)
    employeeCode=models.CharField(max_length=100)
    employeeAddress=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.employeeName