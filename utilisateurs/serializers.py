from rest_framework import serializers
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()


class InscriptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'telephone', 'password', 'role', 'zone']

    def create(self, validated_data):
        # RF-01 : création de compte avec mot de passe chiffré
        user = Utilisateur.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            telephone=validated_data.get('telephone', ''),
            role=validated_data.get('role', Utilisateur.Role.AGRICULTEUR),
            zone=validated_data.get('zone', ''),
            password=validated_data['password'],
        )
        return user


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'telephone', 'role', 'zone', 'est_valide']
        read_only_fields = ['role', 'est_valide']