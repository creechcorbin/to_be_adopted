from django.contrib.auth.models import AbstractUser
from django.db import models
from pets.models import Pet 

# Create your models here.


class AdoptUser(AbstractUser):

   USER_CHOICES = [
       ('AD', 'Adopter'),
       ('SR', 'Shelter/Rescue'),
   ]

   display_name = models.CharField(max_length=50)
   bio = models.TextField()
   account_type = models.CharField(
       max_length=2, choices=USER_CHOICES, default='AD')
   favorites = models.ManyToManyField(Pet, related_name='favorite', symmetrical=False)
 
   def __str__(self):
       return self.display_name
