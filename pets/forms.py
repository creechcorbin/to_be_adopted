from django import forms
from .models import Pet

class AddPetForm(forms.Form):
    PET_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
    ]

    ADOPTION_CHOICES = [
        ('TBA', "To Be Adopted"),
        ('NOA', "Now Officially Adopted"),
    ]
    
    name = forms.CharField(max_length=80)
    age = forms.IntegerField()
    pet_type = forms.ChoiceField(choices=PET_CHOICES)
    bio = forms.CharField(widget=forms.Textarea)
    spayed_or_neutered = forms.BooleanField()
    shot_record = forms.BooleanField()
    status = forms.ChoiceField(choices=ADOPTION_CHOICES)
    pet_image = forms.ImageField(required=False)

