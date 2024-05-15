# admin.py
from django.contrib import admin
from .models import TrackerIncomeExpense

class TrackerIncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'entryType', 'description', 'amount')
    list_filter = ('entryType', 'date')
    search_fields = ('description',)

admin.site.register(TrackerIncomeExpense, TrackerIncomeExpenseAdmin)
