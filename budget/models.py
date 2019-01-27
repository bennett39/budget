from django.conf import settings
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=140)


class Institution(models.Model):
    institution = models.CharField(max_length=140)


class Item(models.Model):
    item = models.CharField(max_length=140)
    long_item = models.CharField(max_length=300)


class BankAccountGroup(models.Model):
    group = models.CharField(max_length=60)


class BankAccount(models.Model):
    pc_accountid = models.CharField(max_length=60)
    name = models.CharField(max_length=140)
    nickname = models.CharField(max_length=140)
    account_type = models.CharField(max_length=140)
    institution = models.ForeignKey(Institution,
            on_delete=models.CASCADE,
            related_name='account_institution')
    account_group = models.ForeignKey(BankAccountGroup,
            on_delete=models.CASCADE, related_name='account_group')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE, related_name='account_user')


class Balance(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE,
            related_name='account_balance')
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    time_refreshed = models.DateTimeField() 


class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE,
            related_name='transaction_account')
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
            related_name='transaction_item')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
            related_name='transaction_category')
    signed_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    pc_transaction_id = models.CharField(max_length=60)
