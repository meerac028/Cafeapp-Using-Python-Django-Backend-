from django.db import models

# Create your models here.

class category_db(models.Model):
    Category_name=models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    profile_image=models.ImageField(upload_to='images',null=True,blank=True)


class product_db(models.Model):
    Category_name=models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    product_image=models.ImageField(upload_to='images',null=True,blank=True)


class login_db(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)