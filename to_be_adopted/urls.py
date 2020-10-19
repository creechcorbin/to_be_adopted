"""to_be_adopted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from authentication.urls import urlpatterns as authurls
from tbauser.urls import urlpatterns as user_urls
from pets.urls import urlpatterns as pet_urls
from notifications.urls import urlpatterns as notif_urls

from pets import views as pet_views
from applications import views as app_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('adopted/', pet_views.sort_adopted),
    path('available/', pet_views.sort_up_for_adoption),
    path('apply/', app_views.pet_app_form_view, name="app_form"),
]

urlpatterns += authurls
urlpatterns += user_urls
urlpatterns += pet_urls
urlpatterns += notif_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

