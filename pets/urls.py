from django.urls import path

from pets import views as pet_views

urlpatterns = [
    path('pet/<int:pet_id>/', pet_views.pet_detail_view, name='pet_detail'),
    path('pet/edit/<int:pet_id>/', pet_views.edit_pet_view),
    path('pet/create/', pet_views.CreatePetProfile.as_view(), name='addpetprofile'),
]
