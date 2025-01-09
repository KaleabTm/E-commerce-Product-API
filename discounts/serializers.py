from rest_framework import serializers

from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class DiscountCreateSerializer(serializers.Serializer):
    product = serializers.UUIDField()
    discount_type = serializers.ChoiceField(choices=["PERCENTAGE", "FLAT"])
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    is_active = serializers.BooleanField()

class DiscountUpdateSerializer(serializers.Serializer):
    discount_type = serializers.ChoiceField(choices=["PERCENTAGE", "FLAT"])
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    is_active = serializers.BooleanField()


class DiscountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "product", "discount_type", "value", "start_date", "end_date"]


class DiscountReactivateSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()



