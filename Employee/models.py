from django.db import models

# Create your models here.



class Employee(models.Model):
                    name=  models.CharField(max_length=50)
                    employee_id = models.CharField(max_length=50)
                    department =  models.CharField(max_length=50)
                    designation= models.CharField(max_length=50)
                    salary = models.IntegerField()
                    image = models.ImageField(upload_to='users',null=True,blank=True)