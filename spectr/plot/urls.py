from django.urls import path,include
from .views import NormalizedView

urlpatterns = [
    path('normalized',NormalizedView.as_view()),
]