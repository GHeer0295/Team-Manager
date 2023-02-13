from django.db import models
from django import forms 
from django.core.validators import RegexValidator
from django.urls import reverse
ROLES = (
    ("Admin", "ADMIN - Can Delete Members"),
    ("Regular", "REGULAR - Can Not Delete Members")
)

class TeamMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # https://stackoverflow.com/questions/60537614/how-do-i-properly-configure-my-app-to-use-the-django-phonenumber-field-module
    phone_number = models.CharField(max_length=12, null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])

    email = models.CharField(max_length=30)    
    role = models.CharField(max_length=7,  choices=ROLES, default='Regular')

    def get_absolute_url(self):
        return reverse('home')