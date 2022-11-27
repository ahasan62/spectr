from django.urls import path,include
from .views import getNormalized,getEmission,getWavelength

urlpatterns = [
    path('normalized',getNormalized),
    path('emission',getEmission),
    path('wavelength',getWavelength),

]