from django import forms
from django.contrib.auth.forms import UserCreationForm
from tbauser.models import AdoptUser


class AdoptUserCreationForm(UserCreationForm):
    class Meta:
        model = AdoptUser
        fields = "__all__"


class Edit(forms.ModelForm):
    class Meta:
        model = AdoptUser
        fields = ['bio', 'email', 'display_name', 'account_type']
