from softy.models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields 
from django.forms import ModelForm

def Entryform(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class meta:
        models=User
        fields= {
            'username'
            'first_name'
            'last_name'
            'email'
            'password1'
            'password2'
        }
        
        def save(self,commit=True):
            user = super(Entryform, self).save(commit=False)
            user.first_name=self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']
            user.email=self.cleaned_data['email']
            
            if commit():
                user.save()
                
            return user

#class SignupForm(forms.ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput)
#
 ##   class Meta:
   #     model = Signup


class BookForm(forms.ModelForm):
    class Meta:
        model = All_Book
        fields = ('title', 'author', 'publisher', 'year', 'uploaded_by', 'desc')


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
        
