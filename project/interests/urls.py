from rest_framework.routers import DefaultRouter
from .views import PointOfInterestViewSet

router = DefaultRouter()
router.register(r'poi', PointOfInterestViewSet, basename='poi')

urlpatterns = router.urls