from django.urls import path

from pets import views as pet_views

urlpatterns = [
    path('pet/<int:pet_id>/', pet_views.pet_detail_view, name='pet_detail'),
    path('pet/edit/<int:pet_id>/', pet_views.edit_pet_view),
    path('pet/create/', pet_views.CreatePetProfile.as_view(), name='addpetprofile'),
    path('favorite/<int:pet_id>/', pet_views.favorite_pet, name='favorite_pet'),
    path('unfavorite/<int:pet_id>/', pet_views.unfavorite_pet, name='unfavorite'),
    path('favorites/<int:user_id>/', pet_views.favorites_view, name='favorites')
]
