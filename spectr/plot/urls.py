from django.urls import path,include
from .views import getNormalized

urlpatterns = [
    path('normalized',getNormalized),
]