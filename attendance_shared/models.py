from django.db import models
from django.core.validators import RegexValidator
from django.core.files import File
import os
# Create your models here.
class Stores(models.Model):
    
        store_id=models.IntegerField()
        branch_id=models.IntegerField()
        address=models.CharField(max_length=255)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        store_mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
        #store_mobile=models.IntegerField()
        store_unique_id=models.IntegerField()
        org_id=models.IntegerField()

class StoreUsers(models.Model):
    
        store_user_id=models.IntegerField()
        store_user_name=models.CharField(max_length=255)
        store_user_pwd=models.CharField(max_length=255)
        org_id=models.IntegerField()
        store_id=models.IntegerField()

class Employees(models.Model):
    
        Employee_id=models.IntegerField()
        Employee_name=models.CharField(max_length=255)
        Employee_Designation=models.CharField(max_length=255)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        Employee_mob=models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
        Gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
        Salary =models.IntegerField()
        Employee_DOB = models.DateField(max_length=8)
        image_file = models.ImageField(upload_to='images')
        Id_Proof= models.URLField()

class Player(models.Model):
    
        Player_id=models.IntegerField()
        Player_name=models.CharField(max_length=255)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        Player_mob=models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
        Gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
        City =models.CharField(max_length=255)
        Player_DOB =models.DateField(max_length=8)
        image_file = models.ImageField(upload_to='images')
        Id_Proof= models.URLField()


class Machines(models.Model):
    
        Game_id=models.IntegerField()
        Player_id=models.CharField(max_length=255)
        
class Player_games(models.Model):
    
        Game_id=models.IntegerField()
        Player_id=models.CharField(max_length=255)
        Game_name= models.CharField(max_length=255)
        Transaction_Choice = (('Bonus-Cash', 'Bonus-Cash'),
        ('Cash-IN', 'Cash-IN'),('Cash-Out', 'Cash-Out'),)
        Transaction_Type = models.CharField(max_length=20, choices=Transaction_Choice)
        Cash_Out_Receipt = models.ImageField(upload_to='images') 
        Machine_Id=models.IntegerField()
        timestamps=models.DateTimeField(auto_now_add=True)



        def __int__(self):
            return self.store_id