from django.shortcuts import render, HttpResponseRedirect, reverse
from pets.models import Pet
from tbauser.models import AdoptUser
from .models import PetApplication
from .forms import PetAppForm
from django import forms

# Create your views here.

def pet_app_form_view(request):
    if request.method == "POST":
        form = PetAppForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data 
            app = PetApplication.objects.create(
                user=request.user,
                full_name=data.get('full_name'),
                address=data.get('address'),
                email=data.get('email'),
                phone=data.get('phone'),
                birthdate=data.get('birthdate'),
                employement=data.get('employment'),
                pet_of_interest=data.get('pet_of_interest'),
                reason_of_interest=data.get('reason_of_interest'),
                own_or_rent=data.get('own_or_rent'),
                additional_info=data.get('additional_info')
            )
            return HttpResponseRedirect(reverse('homepage'))
            
    form = PetAppForm()
    return render(request, 'generic_form.html', {'form': form})