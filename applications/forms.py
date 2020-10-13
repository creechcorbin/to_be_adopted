from django import forms
from .models import PetApplication

class PetAppForm(forms.ModelForm):
    class Meta:
        model = PetApplication
        fields = ['full_name', 'address', 'email', 'phone', 'birthdate', 'employment', 'pet_of_interest', 'reason_of_interest', 'own_or_rent', 'additional_info']
        exclude = ['owner', 'user', 'mark_as_read']