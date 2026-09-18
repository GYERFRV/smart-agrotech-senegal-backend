from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    InscriptionView, ProfilView,
    ListeUtilisateursView, GestionUtilisateurView, StatistiquesView,
)

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('connexion/', TokenObtainPairView.as_view(), name='connexion'),
    path('connexion/refresh/', TokenRefreshView.as_view(), name='connexion_refresh'),
    path('profil/', ProfilView.as_view(), name='profil'),

    # Administration
    path('admin/utilisateurs/', ListeUtilisateursView.as_view(), name='admin_liste_utilisateurs'),
    path('admin/utilisateurs/<int:pk>/', GestionUtilisateurView.as_view(), name='admin_gestion_utilisateur'),
    path('admin/statistiques/', StatistiquesView.as_view(), name='admin_statistiques'),
]