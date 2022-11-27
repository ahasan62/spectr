from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .serializers import NormalizedSerializer, EmissionSerializer, WavelengthSerializer
from .models import Emission, Normalized, Wavelength
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getNormalized(request):
    norm_data = Normalized.objects.all()
    serializer = NormalizedSerializer(norm_data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEmission(request):
    norm_data = Emission.objects.all()
    serializer = EmissionSerializer(norm_data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWavelength(request):
    norm_data = Wavelength.objects.all()
    serializer = WavelengthSerializer(norm_data,many=True)
    return Response(serializer.data)