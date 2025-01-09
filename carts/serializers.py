from rest_framework import serializers

from .models import CartItem, Cart


class CartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "quantity",
            "cart_item_total_price"
        ]


class cartItemSerializer(serializers.Serializer):
    product = serializers.UUIDField()
    quantity = serializers.IntegerField()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemListSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["id", "items", "created_at", "updated_at"]
