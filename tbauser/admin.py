from django.contrib import admin
from .models import AdoptUser
from .forms import AdoptUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdoptUserAdmin(UserAdmin):
    model = AdoptUser
    add_form = AdoptUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Primary Adopter Information',
            {
                'fields': (
                    'display_name',
                    'bio',
                    'account_type'
                )
            }
        )
    )

admin.site.register(AdoptUser, AdoptUserAdmin)