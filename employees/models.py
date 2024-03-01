from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    employee = models.CharField(max_length=20)
    ID_no = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
