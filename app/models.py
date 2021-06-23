from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique= True,default="hostmail@gmail.com")
    password = models.CharField(max_length = 20,default="password")
    employeeid = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class customer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    birthday=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

