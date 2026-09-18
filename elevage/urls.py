from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, SuiviSanitaireViewSet

router = DefaultRouter()
router.register(r'animaux', AnimalViewSet, basename='animal')
router.register(r'suivis-sanitaires', SuiviSanitaireViewSet, basename='suivi-sanitaire')

urlpatterns = router.urls