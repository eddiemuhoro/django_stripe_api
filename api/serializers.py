from .models import  Checkout
from rest_framework import serializers

class CreateCheckoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'user', 'cart', 'total_price', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        checkout = Checkout.objects.create(**validated_data)
        return checkout