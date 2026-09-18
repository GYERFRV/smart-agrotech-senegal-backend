from rest_framework import serializers
from .models import Parcelle


class ParcelleSerializer(serializers.ModelSerializer):
    utilisateur = serializers.ReadOnlyField(source='utilisateur.username')

    class Meta:
        model = Parcelle
        fields = [
            'id', 'utilisateur', 'culture', 'superficie',
            'date_semis', 'statut', 'date_recolte_prevue',
            'rendement', 'date_creation',
        ]
        read_only_fields = ['date_creation']