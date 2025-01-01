from rest_framework import serializers
from .models import ProductImage, Products


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "label"]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ["id", "name", "description", "price", "stock", "category", "images"]


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    created_by = serializers.CharField(source="created_by.email")

    class Meta:
        model = Products
        fields = ["name", "description", "price", "stock", "category", "created_by"]


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    category = serializers.IntegerField()
    created_by = serializers.CharField()
    images = ProductImageSerializer(many=True)
