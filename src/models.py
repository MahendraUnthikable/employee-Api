from django.db import models


class employeeRegistratoin(models.Model):
    """this class contain employee registrtoin
    data and save it to the database.
    """
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.first_name

class employeeDetail(models.Model):
    """this class contain employee profile details,
    and create table in the database.
    """
    employeeName=models.CharField(max_length=100)
    employeeDob=models.DateField(max_length=100)
    employeeEmail=models.EmailField(max_length=100)
    employeePhone=models.CharField(max_length=100)
    employeeCode=models.CharField(max_length=100)
    employeeAddress=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.employeeName