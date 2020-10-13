from django.urls import path

from pets import views as pet_views

urlpatterns = [
    path('pet/<int:pet_id>/', pet_views.pet_detail_view, name='user_detail'),
]
