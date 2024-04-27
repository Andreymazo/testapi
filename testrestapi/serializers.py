from rest_framework import serializers
from testrestapi.models import RealEstateObject

class RealEstateObjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model=RealEstateObject
        fields = [ 'cad_num', 'shirota', 'dolgota']
