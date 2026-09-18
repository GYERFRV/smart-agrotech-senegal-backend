from django.contrib import admin
from .models import Alerte


@admin.register(Alerte)
class AlerteAdmin(admin.ModelAdmin):
    list_display = ('type_risque', 'zone', 'niveau_risque', 'date')
    list_filter = ('type_risque', 'niveau_risque', 'zone')