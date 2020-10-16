from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AddPetForm
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pets.models import Pet

# Create your views here.

# Similiar to GhostPost filter boasts/roasts

# Add reverse inside of HTTPRedirect
# Add html part to filter functions


def pet_detail_view(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)
    
    return render(request, 'pet_detail.html', {'selected_pet': selected_pet})


def edit_pet_view(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)

    if request.method == 'POST':
        form = AddPetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            age = data['age']
            pet_type = data['pet_type']
            bio = data['bio']
            spayed_or_neutered = data['spayed_or_neutered']
            shot_record = data['shot_record']
            status = data['status']
            pet_image = data['pet_image']
        return HttpResponseRedirect(reverse('pet_detail', args=[selected_pet.id]))
    
    data = {
        'name': selected_pet.name,
        'age': selected_pet.age,
        'pet_type': selected_pet.pet_type,
        'bio': selected_pet.bio,
        'spayed_or_neutered': selected_pet.spayed_or_neutered,
        'shot_record': selected_pet.shot_record,
        'status': selected_pet.status,
        'pet_image': selected_pet.pet_image,
    }

    form = AddPetForm(initial=data)

    return render(request, 'edit_pet.html', {'form': form})


def favorites_pets(request, id):
    pet = Pet.objects.get(id=id)
    current_user = request.user
    current_user.favorites.add(pet)

    return HttpResponseRedirect('homepage')


def sort_adopted(request):
    data = Pet.objects.filter(status=2)
    return render(request, "homepage.html", {'data': data})


def sort_up_for_adoption(request):
    data = Pet.objects.filter(status=1)
    return render(request, "homepage.html" , {'data': data})


class CreatePetProfile(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = AddPetForm()
        return render(request, 'generic_form.html', {'form': form })

    def post(self, request):
        if request.user.account_type == "SR":
            form = AddPetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                profile = Pet.objects.create(
                    name=data.get("name"),
                    age=data.get("age"),
                    pet_type=data.get('pet_type'),
                    bio=data.get('bio'),
                    spayed_or_neutered=data.get('spayed_or_neutered'),
                    shot_record=data.get('shot_record'),
                    status=data.get('status'),
                    pet_image=data.get('pet_image'),
                    owner=request.user
                )
                profile.save()
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return render(request, 'generic_form.html', {'form': form })