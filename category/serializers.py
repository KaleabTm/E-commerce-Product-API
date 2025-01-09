from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class CategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()