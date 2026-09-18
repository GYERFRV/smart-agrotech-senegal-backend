from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import InscriptionSerializer, UtilisateurSerializer
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()


class EstAdmin(permissions.BasePermission):
    """Autorise seulement les administrateurs"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == Utilisateur.Role.ADMIN or request.user.is_superuser
        )


class InscriptionView(generics.CreateAPIView):
    """RF-01 : Création de compte"""
    queryset = Utilisateur.objects.all()
    serializer_class = InscriptionSerializer
    permission_classes = [permissions.AllowAny]


class ProfilView(generics.RetrieveUpdateAPIView):
    """RF-05 : Consultation et modification du profil"""
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ListeUtilisateursView(generics.ListAPIView):
    """RF-20 : L'administrateur consulte la liste de tous les utilisateurs"""
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [EstAdmin]


class GestionUtilisateurView(generics.RetrieveUpdateDestroyAPIView):
    """RF-21 : L'administrateur modifie, suspend ou supprime un compte"""
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [EstAdmin]


class StatistiquesView(APIView):
    """RF-23 : Statistiques globales d'utilisation de la plateforme"""
    permission_classes = [EstAdmin]

    def get(self, request):
        from cultures.models import Parcelle
        from elevage.models import Animal
        from meteo.models import Alerte
        from marche.models import Annonce

        data = {
            'total_utilisateurs': Utilisateur.objects.count(),
            'total_agriculteurs': Utilisateur.objects.filter(role='AGRICULTEUR').count(),
            'total_acheteurs': Utilisateur.objects.filter(role='ACHETEUR').count(),
            'total_parcelles': Parcelle.objects.count(),
            'total_animaux': Animal.objects.count(),
            'total_alertes': Alerte.objects.count(),
            'total_annonces': Annonce.objects.count(),
            'annonces_disponibles': Annonce.objects.filter(statut='DISPONIBLE').count(),
        }
        return Response(data)