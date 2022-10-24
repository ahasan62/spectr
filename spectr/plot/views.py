from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .serializers import NormalizedSerializer
from .models import Normalized
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getNormalized(request):
    norm_data = Normalized.objects.all()
    serializer = NormalizedSerializer(norm_data,many=True)
    return Response(serializer.data)

