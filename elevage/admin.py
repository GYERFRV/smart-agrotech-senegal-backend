from django.contrib import admin
from .models import Animal, SuiviSanitaire


class SuiviSanitaireInline(admin.TabularInline):
    model = SuiviSanitaire
    extra = 1


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'espece', 'utilisateur', 'nombre', 'date_naissance')
    list_filter = ('espece',)
    search_fields = ('identifiant', 'utilisateur__username')
    inlines = [SuiviSanitaireInline]


@admin.register(SuiviSanitaire)
class SuiviSanitaireAdmin(admin.ModelAdmin):
    list_display = ('animal', 'type_intervention', 'date', 'prochaine_echeance')
    list_filter = ('type_intervention',)