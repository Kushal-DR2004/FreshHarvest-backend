from django.shortcuts import render
from .models import Farmer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .serializers import FarmerWithFarmSerializer , FarmerSimpleSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Farmer.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return FarmerSimpleSerializer
        return FarmerWithFarmSerializer
