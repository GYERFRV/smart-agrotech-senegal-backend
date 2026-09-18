from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        AGRICULTEUR = 'AGRICULTEUR', 'Agriculteur / Éleveur'
        ACHETEUR = 'ACHETEUR', 'Acheteur'
        ADMIN = 'ADMIN', 'Administrateur'

    telephone = models.CharField(max_length=20, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.AGRICULTEUR,
    )
    zone = models.CharField(max_length=100, blank=True, help_text="Région ou zone géographique")
    est_valide = models.BooleanField(default=True, help_text="Compte validé par l'administrateur (RF-03)")

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilisateurs',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilisateurs_permissions',
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"