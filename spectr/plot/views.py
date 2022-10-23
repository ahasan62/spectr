from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .serializers import NormalizedSerializer
from .models import Normalized
# Create your views here.

class NormalizedView(generics.CreateAPIView):
    queryset = Normalized.objects.all()
    serializer_class = NormalizedSerializer

