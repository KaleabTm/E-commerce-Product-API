from rest_framework import serializers
from .models import ProductImage, Products

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'label']

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'is_popular', 'is_latest', 'images']

    # def create(self, validated_data):
    #     images_data = validated_data.pop('images', [])
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'category', 'created_by']
