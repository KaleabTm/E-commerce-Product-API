from rest_framework import serializers

from .models import CartItem, Cart


class CartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "product",
            "quantity",
            "discounted_price",
            "item_total_price",
        ]


class cartItemCreateSerializer(serializers.Serializer):
    cart = serializers.CharField()
    product = serializers.CharField()
    quantity = serializers.IntegerField()


class CartItemUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "discounted_price", "item_total_price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "created_at", "updated_at"]
