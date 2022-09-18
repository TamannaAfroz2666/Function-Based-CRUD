from dataclasses import field
from pyexpat import model
from tkinter.ttk import Widget
from unicodedata import name
from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        # Widgets = {
        #     'name': forms.NumberInput(attrs={'class':'form-control'}), 
        #     'email': forms.EmailInput(attrs={'class':'form-control'}), 
        #     'password': forms.PasswordInput(), 
        # }

        