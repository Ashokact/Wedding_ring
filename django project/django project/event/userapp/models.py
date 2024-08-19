from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    
    

    
