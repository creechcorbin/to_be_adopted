from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from tbauser.views import user_detail_view, edit_user_view


urlpatterns = [
    path('user/<int:user_id>/', user_detail_view, name='user_detail'),
    path('edit/<int:user_id>/', edit_user_view, name='edit_user'),
]
