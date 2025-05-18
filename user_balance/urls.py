from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/balance/<int:user_id>', UserBalanceView.as_view(), name='balance'),
    path('api/v1/deposit/<int:user_id>', DepositView.as_view(), name='deposit'),
    path('api/v1/withdraw/<int:user_id>', WithdrawView.as_view(), name='withdraw'),
    path('api/v1/transfer/<int:from_user_id>', TransferView.as_view(), name='transfer'),
]