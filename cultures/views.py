from rest_framework import viewsets, permissions
from .models import Parcelle
from .serializers import ParcelleSerializer


class ParcelleViewSet(viewsets.ModelViewSet):
    """
    RF-06 à RF-09 : gestion des parcelles
    - Liste/ajoute/modifie/supprime les parcelles de l'utilisateur connecté
    """
    serializer_class = ParcelleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Chaque utilisateur ne voit que SES parcelles
        return Parcelle.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        # Associe automatiquement la parcelle à l'utilisateur connecté
        serializer.save(utilisateur=self.request.user)