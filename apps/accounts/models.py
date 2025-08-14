from django.db import models
from apps.university.models import Department , Branch , University
import os 

def profile_images(instance,filename):
    return os.path.join('profile_images',instance.username,filename)

class User(models.Model):

    class Meta:
        ordering = ['-created_at']
        db_table = 'userprofile'

    YEAR_CHOCIES = (
        ('1','First Year'),
        ('2','Second Year'),
        ('3','Third Year'),
        ('4','Fourth Year'),
    )

    GENDER_CHOICES = (
        ('M' , 'Male'),
        ('F' , 'Female'),
        ('O' , 'Other'),
    )
    username = models.CharField(max_length=25,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    profile_pic = models.ImageField(upload_to=profile_images , blank=True , null=True)
    university_name = models.ForeignKey(University,on_delete=models.SET_NULL,null=True)
    university_email = models.EmailField(unique=True,help_text="Use Your University Email Address")
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name='students')
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True,related_name='students')
    year = models.CharField(max_length=20,choices=YEAR_CHOCIES)
    bio = models.TextField(max_length=250,blank=True,help_text="Tell Others About Yourself")
    current_password = models.CharField(max_length = 25)
    previous_password = models.CharField(max_length = 25,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

