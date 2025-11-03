# country\views.py

from django.shortcuts import render

from rest_framework import viewsets
from .models import Citizen
from .serializers import CitizenSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

