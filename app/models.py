from django.db import models


# Create your models here.


    
class student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    standerd=models.IntegerField()
    city=models.CharField(max_length=100)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    
class user(models.Model):
    name=models.CharField( max_length=50)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=100)
    
    

    
    
    
class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    stok=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    

    
