from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password 
from django import forms
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,default='0000000')
    email = models.CharField(max_length=122,default='0000000')
    phone = models.CharField(max_length=12,default='0000000')
    desc = models.TextField(default='0000000')
    

    def __str__(self):
        return self.name

#class Signup(models.Model):
   # user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
   # email = models.CharField(max_length=122,default='Email')
   # first_name = models.CharField(max_length=122,default='First Name')
   # last_name = models.CharField(max_length=122,default='Last Name')
    
    #def __str__(self):
    #    return self.first_name

#class profile(models.Model):
#    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#    Firstname = models.CharField(max_length=122,default='first name')
#    username = models.CharField(max_length=122,default='username')
#    password = models.CharField(max_length=122,default='password')
    
#    def __str__(self):
#        return str(self.user) 



class Act_Adv(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='Act_Adv/pdfs/')
    cover = models.ImageField(upload_to='Act_Adv/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class Classics(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='Classics/pdfs')
    cover = models.ImageField(upload_to='Classics/covers', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class CBGN(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='CBGN/pdfs/')
    cover = models.ImageField(upload_to='CBGN/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class DM(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='DM/pdfs/')
    cover = models.ImageField(upload_to='DM/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class Fantasy(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='Fantasy/pdfs/')
    cover = models.ImageField(upload_to='Fantasy/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class HF(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='HF/pdfs/')
    cover = models.ImageField(upload_to='HF/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class Horror(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='Horror/pdfs/')
    cover = models.ImageField(upload_to='Horror/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class LF(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='LF/pdfs/')
    cover = models.ImageField(upload_to='LF/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class Sci_fi(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='Sci-fi/pdfs/')
    cover = models.ImageField(upload_to='Sci-fi/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title

class All_Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.TextField(default='Description')
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='AllBook/pdfs/')
    cover = models.ImageField(upload_to='AllBook/covers/', null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
         return self.title




class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
   
