from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from pets.views import pet_detail_view

urlpatterns = [
    path('pet/<int:pet_id>/', pet_detail_view, name='user_detail'),
]