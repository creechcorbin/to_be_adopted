from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AddPetForm, EditPet
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from pets.models import Pet
from notifications.models import Notification
from tbauser.models import AdoptUser


@login_required
def pet_detail_view(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)
    try:
        selected_pet 
    except Pet.DoesNotExist:
        return render(request, "404.html", status=404)
    
    current_user = request.user
    favorited_pet = False
    user_favs = current_user.favorites.all()
    for pet in user_favs:
        if pet == selected_pet:
            favorited_pet = True
    
    return render(request, 'pet_detail.html', {'selected_pet': selected_pet, 'favorited_pet': favorited_pet})



def edit_pet_view(request, pet_id):
    form = None
    html = 'edit_pet.html'
    instance = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        form = EditPet(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('pet_detail', args=[instance.id]))
    else:
        form = EditPet(instance=instance)
        return render(request, html, {'form': form})

def favorite_pet(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)
    current_user = request.user
    current_user.favorites.add(selected_pet)
    owner = selected_pet.owner
    notification = Notification.objects.create(
        owner_of_favorited=owner,
        favorited_pet=selected_pet
        )

    return HttpResponseRedirect(reverse('homepage'))
    

def unfavorite_pet(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)
    current_user = request.user
    current_user.favorites.remove(selected_pet)

    return HttpResponseRedirect(reverse('homepage'))


def favorites_view(request, user_id):
    current_user = AdoptUser.objects.get(id=user_id)
    user_favs = current_user.favorites.all()

    return render(request, "favorites.html", {'current_user': current_user, 'user_favs': user_favs})


def sort_adopted(request):
    data = Pet.objects.filter(status='NOA')
    return render(request, "adopted.html", {'data': data})


def sort_up_for_adoption(request):
    data = Pet.objects.filter(status='TBA')
    return render(request, "available.html" , {'data': data})


class CreatePetProfile(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = AddPetForm()
        return render(request, 'create_pet.html', {'form': form })

    def post(self, request):
        if request.user.account_type == "SR":
            form = AddPetForm(request.POST, request.FILES)
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
                return render(request, 'create_pet.html', {'form': form })
