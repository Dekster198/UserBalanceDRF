from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.IntegerField(blank=False, default=0, verbose_name='Баланс')

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withddraw(self, amount):
        if self.balance < amount:
            raise ValueError('Недостаточно средств для совершения данной операции')

        self.balance -= amount
        self.save()

    def transfer(self, amount, to_user):
        self.withddraw(amount)
        to_user.deposit(amount)
