from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Animal(models.Model):
    class Espece(models.TextChoices):
        BOVIN = 'BOVIN', 'Bovin'
        OVIN = 'OVIN', 'Ovin'
        CAPRIN = 'CAPRIN', 'Caprin'
        VOLAILLE = 'VOLAILLE', 'Volaille'
        AUTRE = 'AUTRE', 'Autre'

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='animaux',
    )
    identifiant = models.CharField(max_length=50, help_text="Identifiant de l'animal ou du lot")
    espece = models.CharField(max_length=20, choices=Espece.choices, default=Espece.BOVIN)
    date_naissance = models.DateField(null=True, blank=True)
    nombre = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Nombre d'animaux dans le lot (si applicable)"
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identifiant} - {self.get_espece_display()} ({self.utilisateur.username})"

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Animal / Lot"
        verbose_name_plural = "Animaux / Lots"


class SuiviSanitaire(models.Model):
    class TypeIntervention(models.TextChoices):
        VACCIN = 'VACCIN', 'Vaccination'
        TRAITEMENT = 'TRAITEMENT', 'Traitement'
        VISITE = 'VISITE', 'Visite vétérinaire'

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='suivis_sanitaires',
    )
    type_intervention = models.CharField(max_length=20, choices=TypeIntervention.choices)
    date = models.DateField()
    prochaine_echeance = models.DateField(null=True, blank=True, help_text="Date du prochain rappel (RF-12)")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_intervention_display()} - {self.animal.identifiant} ({self.date})"

    class Meta:
        ordering = ['-date']
        verbose_name = "Suivi sanitaire"
        verbose_name_plural = "Suivis sanitaires"