from rest_framework import serializers
from .models import Animal, SuiviSanitaire


class SuiviSanitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuiviSanitaire
        fields = ['id', 'animal', 'type_intervention', 'date', 'prochaine_echeance', 'notes']


class AnimalSerializer(serializers.ModelSerializer):
    utilisateur = serializers.ReadOnlyField(source='utilisateur.username')
    suivis_sanitaires = SuiviSanitaireSerializer(many=True, read_only=True)

    class Meta:
        model = Animal
        fields = [
            'id', 'utilisateur', 'identifiant', 'espece',
            'date_naissance', 'nombre', 'date_creation',
            'suivis_sanitaires',
        ]
        read_only_fields = ['date_creation']