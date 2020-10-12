from django.urls import path

from pets import views

urlpatterns = [
    path('favorite/<int:id>/', views.favorites_pets),
    path('adopted/', views.sort_adopted),
    path('unadopted/', views.sort_up_for_adoption),
]
