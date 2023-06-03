from rest_framework import serializers
from home.models import Emp
class Empserializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields="__all__"