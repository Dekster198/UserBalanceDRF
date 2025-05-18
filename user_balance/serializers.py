from rest_framework import serializers
from .models import User


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'balance']


class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)


class WithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)


class TransferSerializer(serializers.Serializer):
    to_user = serializers.IntegerField()
    amount = serializers.IntegerField(min_value=1)
