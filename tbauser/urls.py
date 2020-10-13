from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from tbauser.views import user_detail_view

urlpatterns = [
    path('user/<int:user_id>/', user_detail_view, name='user_detail'),
]