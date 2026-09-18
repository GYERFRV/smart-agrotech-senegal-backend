from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Annonce(models.Model):
    class Statut(models.TextChoices):
        DISPONIBLE = 'DISPONIBLE', 'Disponible'
        VENDU = 'VENDU', 'Vendu'
        SUSPENDU = 'SUSPENDU', 'Suspendu'

    class Categorie(models.TextChoices):
        CEREALES = 'CEREALES', 'Céréales'
        LEGUMES = 'LEGUMES', 'Légumes'
        FRUITS = 'FRUITS', 'Fruits'
        BETAIL = 'BETAIL', 'Bétail'
        AUTRE = 'AUTRE', 'Autre'

    vendeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='annonces',
    )
    titre = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    prix = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Prix en FCFA"
    )
    categorie = models.CharField(max_length=20, choices=Categorie.choices, default=Categorie.AUTRE)
    zone = models.CharField(max_length=100, blank=True, help_text="Zone géographique du vendeur")
    photo = models.ImageField(upload_to='annonces/', null=True, blank=True)
    statut = models.CharField(max_length=20, choices=Statut.choices, default=Statut.DISPONIBLE)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.prix} FCFA ({self.get_statut_display()})"

    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Annonce"
        verbose_name_plural = "Annonces"