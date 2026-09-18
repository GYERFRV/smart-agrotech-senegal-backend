from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Parcelle(models.Model):
    class StatutCulture(models.TextChoices):
        SEMIS = 'SEMIS', 'Semis'
        CROISSANCE = 'CROISSANCE', 'Croissance'
        RECOLTE = 'RECOLTE', 'Récolte'

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='parcelles',
    )
    culture = models.CharField(max_length=100, help_text="Type de culture (ex: mil, arachide, maïs)")
    superficie = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Superficie en hectares"
    )
    date_semis = models.DateField()
    statut = models.CharField(
        max_length=20,
        choices=StatutCulture.choices,
        default=StatutCulture.SEMIS,
    )
    date_recolte_prevue = models.DateField(null=True, blank=True)
    rendement = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(0)],
        help_text="Rendement en kg, renseigné après récolte"
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.culture} - {self.utilisateur.username} ({self.superficie} ha)"

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Parcelle"
        verbose_name_plural = "Parcelles"