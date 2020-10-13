from django import forms
from tbauser.models import AdoptUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdoptUser
        fields = ['display_name', 'account_type']