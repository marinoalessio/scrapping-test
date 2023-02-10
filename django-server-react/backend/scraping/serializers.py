from rest_framework import serializers
from .models import Boat

# This code specifies the model to work with and the fields to be converted to JSON

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ('title', 'price') 
