from django.db import models
from pets.models import Pet
from tbauser.models import AdoptUser


class Notification(models.Model):
    owner_of_favorited = models.ForeignKey(AdoptUser, on_delete=models.CASCADE)
    favorited_pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)



