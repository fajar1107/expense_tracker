# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class TrackerIncomeExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate each entry with a user
    date = models.DateField()
    ENTRY_TYPE = (
        ('income', 'INCOME'),
        ('expense', 'EXPENSE')
    )
    entryType = models.CharField(max_length=10, choices=ENTRY_TYPE, default='income')
    description = models.CharField(max_length=255)
    amount = models.IntegerField()