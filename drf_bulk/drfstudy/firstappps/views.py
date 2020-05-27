from django.shortcuts import render
from .serializers import PersonSerializer,ProfessionSerializer
from .models import Person,Profession
from rest_framework import viewsets

class PersonViewSets(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class ProfessionViewSets(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()
