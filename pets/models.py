from django.db import models
from django.utils import timezone
from to_be_adopted.settings import AUTH_USER_MODEL

# Create your models here.


class Pet(models.Model):
  PET_CHOICES = [
    ('DOG', 'Dog'),
    ('CAT', 'Cat'),
      ]

  ADOPTION_CHOICES = [
    ('TBA', "To Be Adopted"),
    ('NOA', "Now Officially Adopted"),
      ]

  name = models.CharField(max_length=80)
  age = models.IntegerField()
  pet_type = models.CharField(
      max_length=3, choices=PET_CHOICES, default="DOG")
  post_date = models.DateField(default=timezone.now)
  bio = models.TextField()
  spayed_or_neutered = models.BooleanField(default=False)
  shot_record = models.BooleanField(default=False)
  status = models.CharField(max_length=3, blank=True,
                            choices=ADOPTION_CHOICES, default='TBA')
  pet_image = models.ImageField(null=True, blank=True)
  owner = models.ForeignKey(AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE, null=True)
  
  def __str__(self):
      return f"{self.name} ({self.pet_type})"
    