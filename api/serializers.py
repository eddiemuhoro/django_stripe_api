from .models import Product, Cart, CartItem, Checkout
from rest_framework import serializers

class CreateCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'user', 'cart', 'total_price', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        checkout = Checkout.objects.create(**validated_data)
        return checkout