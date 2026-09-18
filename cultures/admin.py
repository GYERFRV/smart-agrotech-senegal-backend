from django.contrib import admin
from .models import Parcelle


@admin.register(Parcelle)
class ParcelleAdmin(admin.ModelAdmin):
    list_display = ('culture', 'utilisateur', 'superficie', 'statut', 'date_semis', 'date_recolte_prevue')
    list_filter = ('statut', 'culture')
    search_fields = ('culture', 'utilisateur__username')