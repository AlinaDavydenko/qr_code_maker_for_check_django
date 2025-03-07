from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price']


# Сериализатор для обработки POST-запроса
class CashMachineRequestSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())
