from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'telephone', 'zone', 'est_valide', 'is_active')
    list_filter = ('role', 'est_valide', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Smart AgroTech', {'fields': ('telephone', 'role', 'zone', 'est_valide')}),
    )