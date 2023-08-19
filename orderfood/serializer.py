from rest_framework import serializers

from orderfood.models import OrderFood


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'
