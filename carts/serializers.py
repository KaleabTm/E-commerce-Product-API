from rest_framework import serializers

from .models import CartItem, Cart


class CartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "quantity"
        ]


class cartItemSerializer(serializers.Serializer):
    product = serializers.UUIDField()
    quantity = serializers.UUIDField()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemListSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["id", "user", "items", "created_at", "updated_at"]
