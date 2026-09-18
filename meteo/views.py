from rest_framework import viewsets, permissions
from .models import Alerte
from .serializers import AlerteSerializer


class AlerteViewSet(viewsets.ModelViewSet):
    """
    RF-13/RF-14 : affichage des prévisions et alertes
    RF-15 : historique des alertes reçues par utilisateur
    """
    serializer_class = AlerteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Un admin voit toutes les alertes ; un utilisateur normal ne voit
        # que celles qui lui sont destinées (RF-15)
        if user.role == user.Role.ADMIN or user.is_superuser:
            return Alerte.objects.all()
        return Alerte.objects.filter(destinataires=user)