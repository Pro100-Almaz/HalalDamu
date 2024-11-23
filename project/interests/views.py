from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

class PointOfInterestViewSet(ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    filter_backends = [SearchFilter]
    search_fields = ['category']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset
