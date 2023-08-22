from rest_framework import serializers

from orderfood.models import OrderFood, Food


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
