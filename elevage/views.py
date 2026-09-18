from rest_framework import viewsets, permissions
from .models import Animal, SuiviSanitaire
from .serializers import AnimalSerializer, SuiviSanitaireSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """RF-10 : fiche d'identification de chaque animal ou lot"""
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)


class SuiviSanitaireViewSet(viewsets.ModelViewSet):
    """RF-11 : interventions sanitaires / RF-12 : rappels d'échéance"""
    serializer_class = SuiviSanitaireSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ne montre que les suivis liés aux animaux de l'utilisateur connecté
        return SuiviSanitaire.objects.filter(animal__utilisateur=self.request.user)