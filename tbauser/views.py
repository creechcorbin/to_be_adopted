from django.shortcuts import render
from tbauser.models import AdoptUser

# Create your views here.

def user_detail_view(request, user_id):
    selected_user = AdoptUser.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'selected_user': selected_user})