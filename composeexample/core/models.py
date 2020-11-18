from django.db import models

# Create your models here.

class Name(models.Model):
    
    first_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)

class Number(models.Model):
    
    number = models.IntegerField()



