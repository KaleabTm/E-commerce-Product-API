from rest_framework import serializers

from orders.models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "status",
            "has_paid",
            "items",
            "created_at",
            "updated_at",
        ]


class OrderCreateSerializer(serializers.Serializer):
    user = serializers.CharField()
    product = serializers.CharField()
    quantity = serializers.IntegerField()
