from rest_framework import serializers
from .models import EPaper


class EPaperSerializer(serializers.ModelSerializer):
    class Meta():
        model = EPaper
        fields = '__all__'