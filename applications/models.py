from django.db import models
from tbauser.models import AdoptUser
from pets.models import Pet

# Create your models here.

class PetApplication(models.Model):
    HOUSE_CHOICES = [
        ("OWN", "Own"),
        ("RENT", "Rent"),
    ]

    REASON_CHOICES = [
        ("FAMP","Family Pet"),
        ("PCHI","Pet For Child"),
        ("WTCH","Watchdog"),
        ("COMP","Companion"),
        ("BRED","Breeding"),
        ("HUNT","Hunting Dog"),
        ("GURD","Guard Dog"),
        ("BARN","Barn Cat/Mouser"),
        ("PCOM","Pet Companion"),
    ]
    user = models.ForeignKey(AdoptUser, related_name="interested_user", on_delete=models.CASCADE)
    owner = models.ForeignKey(AdoptUser, related_name="current_owner", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=240, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    employment = models.TextField(blank=True)
    pet_of_interest = models.ForeignKey(Pet, related_name="pet_of_interest", on_delete=models.CASCADE)
    reason_of_interest = models.CharField(max_length=5, choices=REASON_CHOICES)
    own_or_rent = models.CharField(max_length=5, choices=HOUSE_CHOICES)
    additional_info = models.TextField(null=True)
    mark_as_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}'s Pet Application Form for {self.pet_of_interest}"