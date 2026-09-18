from rest_framework import viewsets, permissions
from .models import Annonce
from .serializers import AnnonceSerializer


class AnnonceViewSet(viewsets.ModelViewSet):
    """
    RF-16 : publication d'annonces
    RF-17 : recherche/filtrage
    RF-18 : contact vendeur (via les infos du vendeur dans la réponse)
    RF-19 : modification/suppression par le vendeur
    """
    serializer_class = AnnonceSerializer

    def get_permissions(self):
        # RF-17 : tout le monde (même visiteur) peut consulter le marché
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        # Pour publier/modifier/supprimer, il faut être connecté
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Annonce.objects.all()
        # RF-17 : filtrage par catégorie, zone, prix via l'URL
        # ex: /api/marche/annonces/?categorie=CEREALES&zone=Thies
        categorie = self.request.query_params.get('categorie')
        zone = self.request.query_params.get('zone')
        prix_max = self.request.query_params.get('prix_max')

        if categorie:
            queryset = queryset.filter(categorie=categorie)
        if zone:
            queryset = queryset.filter(zone__icontains=zone)
        if prix_max:
            queryset = queryset.filter(prix__lte=prix_max)

        return queryset

    def perform_create(self, serializer):
        serializer.save(vendeur=self.request.user)