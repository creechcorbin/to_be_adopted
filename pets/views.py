from django.shortcuts import render, HttpResponseRedirect

from pets.models import Pet

# Create your views here.

# Similiar to GhostPost filter boasts/roasts

# Add reverse inside of HTTPRedirect
# Add html part to filter functions


def favorites_pets(request, id):
    pet = Pet.objects.get(id=id)
    current_user = request.user
    current_user.favorites.add(pet)

    return HttpResponseRedirect('/')


def sort_adopted(request):
    data = Pet.objects.filter(status=2)
    return render(request, , {'data': data})


def sort_up_for_adoption(request):
    data = Pet.objects.filter(status=1)
    return render(request, , {'data': data})