from rest_framework import serializers
from pins.models import Pin, PinCategory


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ("id", "img", "category", "user")


class PinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PinCategory
        fields = ("id", "name")
