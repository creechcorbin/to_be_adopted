from django.contrib import admin
from django.urls import path

from authentication.views import index_view, SignupView, login_view, logout_view


urlpatterns = [
    path('', index_view, name='homepage'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]