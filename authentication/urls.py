from django.contrib import admin
from django.urls import path

from authentication import views as v


urlpatterns = [
    path('', v.index, name='homepage'),
    path('signup/', v.SignupView.as_view() , name='signup'),
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout'),
]