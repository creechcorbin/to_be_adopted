from django.shortcuts import render

from pets.models import Pet

# Create your views here.

def pet_detail_view(request, pet_id):
    selected_pet = Pet.objects.get(id=pet_id)

    return render(request, 'pet_detail.html', {'selected_pet': selected_pet})