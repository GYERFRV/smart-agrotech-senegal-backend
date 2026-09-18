from rest_framework import serializers
from .models import Alerte


class AlerteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerte
        fields = [
            'id', 'type_risque', 'zone', 'niveau_risque',
            'conseil', 'date', 'destinataires',
        ]
        read_only_fields = ['date']