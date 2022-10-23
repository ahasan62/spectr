from rest_framework import serializers
from .models import Normalized
from .models import Emission
from .models import Wavelength
class NormalizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Normalized
        fields = ('molecule','isocode','velocity','thermal','profile','temperature','log_columndensity','normalized') 


class EmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emission
        fields = ('molecule','isocode','velocity','thermal','profile','temperature','log_columndensity','emission') 


class WavelengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wavelength
        fields = ('oversampling','resolution','wavelength') 

