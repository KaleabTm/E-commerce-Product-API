from rest_framework import serializers

from orders.models import OrderItem


class OrderItemListSerializer():
    class Meta:
        model= OrderItem
        fields= '__all__'