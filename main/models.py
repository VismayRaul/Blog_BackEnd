from distutils.command.upload import upload
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class User_Registration(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='img/')
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)


class User_Blog(models.Model):
    Blog_Image = models.ImageField(upload_to='Blog_img/')
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=100)
    Description = models.TextField()
    Created_At = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User_Registration, on_delete=models.CASCADE)














