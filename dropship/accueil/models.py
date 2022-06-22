from itertools import product
from pickle import TRUE
from unicodedata import category
from django.db import models

class order(models.Model):
     id=models.AutoField(blank=False,primary_key=True)
     product=models.CharField(max_length=50,blank=False)
     category=models.CharField(max_length=50)
     quantité=models.IntegerField()
     order_by=models.CharField(max_length=50)
     def __str__(self):
        return self.order_by
    
class staff(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    first=models.CharField(max_length=50,blank=False,default="anonymous")
    last=models.CharField(max_length=50,blank=False,default="anonymous")
    handel=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.handel
class product(models.Model):
    id = models.AutoField(blank=False,primary_key=True)
    product=models.CharField(max_length=50,blank=False)
    category=models.CharField(max_length=50)
    quantité=models.IntegerField()
    activity=models.BooleanField(null=True)
    def __str__(self):
        return self.product
class profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    adress=models.CharField(max_length=50)