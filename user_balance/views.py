from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import *


class UserBalanceView(APIView):
    """Получение баланса пользователя"""
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserBalanceSerializer(user)

        return Response({'status': 'success', 'balance': serializer.data})


class DepositView(APIView):
    """Пополнение баланса пользователя"""
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.deposit(serializer.validated_data['amount'])

        return Response({'status': 'success', 'balance': user.balance})


class WithdrawView(APIView):
    """Снятие денег с баланса пользователя"""
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = WithdrawSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user.withddraw(serializer.validated_data['amount'])

            return Response({'status': 'success', 'balance': user.balance})
        except ValueError as e:
            return Response({'status': 'error', 'message': str(e)})


class TransferView(APIView):
    """Перевод денег с одного баланса на другой"""
    def post(self, request, from_user_id):
        user = get_object_or_404(User, id=from_user_id)
        serializer = TransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        to_user = get_object_or_404(User, id=serializer.validated_data['to_user'])
        amount = serializer.validated_data['amount']

        try:
            user.transfer(to_user, amount)

            return Response({'status': 'success', 'from_user_balance': user.balance, 'to_user_balance': to_user.balance})
        except ValueError as e:
            return Response({'status': 'error', 'message': str(e)})
