from django.contrib import admin
from .models import Annonce


@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'vendeur', 'prix', 'categorie', 'statut', 'date_publication')
    list_filter = ('categorie', 'statut')
    search_fields = ('titre', 'vendeur__username')