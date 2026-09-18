from django.conf import settings
from django.db import models


class Alerte(models.Model):
    class TypeRisque(models.TextChoices):
        SECHERESSE = 'SECHERESSE', 'Sécheresse'
        FORTES_PLUIES = 'FORTES_PLUIES', 'Fortes pluies'
        VENTS_VIOLENTS = 'VENTS_VIOLENTS', 'Vents violents'
        VAGUE_CHALEUR = 'VAGUE_CHALEUR', 'Vague de chaleur'
        AUTRE = 'AUTRE', 'Autre'

    class NiveauRisque(models.TextChoices):
        FAIBLE = 'FAIBLE', 'Faible'
        MOYEN = 'MOYEN', 'Moyen'
        ELEVE = 'ELEVE', 'Élevé'

    type_risque = models.CharField(max_length=30, choices=TypeRisque.choices)
    zone = models.CharField(max_length=100, help_text="Région ou zone géographique concernée")
    niveau_risque = models.CharField(max_length=10, choices=NiveauRisque.choices, default=NiveauRisque.MOYEN)
    conseil = models.TextField(blank=True, help_text="Recommandation associée (ex: irrigation)")
    date = models.DateTimeField(auto_now_add=True)

    # Utilisateurs ayant reçu cette alerte (pour RF-15, historique par utilisateur)
    destinataires = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='alertes_recues',
        blank=True,
    )

    def __str__(self):
        return f"{self.get_type_risque_display()} - {self.zone} ({self.get_niveau_risque_display()})"

    class Meta:
        ordering = ['-date']
        verbose_name = "Alerte"
        verbose_name_plural = "Alertes"