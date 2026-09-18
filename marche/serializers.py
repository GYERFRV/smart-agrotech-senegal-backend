from rest_framework import serializers
from .models import Annonce


class AnnonceSerializer(serializers.ModelSerializer):
    vendeur = serializers.ReadOnlyField(source='vendeur.username')

    class Meta:
        model = Annonce
        fields = [
            'id', 'vendeur', 'titre', 'description', 'prix',
            'categorie', 'zone', 'photo', 'statut', 'date_publication',
        ]
        read_only_fields = ['date_publication']