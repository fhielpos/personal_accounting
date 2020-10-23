from django.contrib import admin

# Register your models here.

from .models import Bank, BankExpense, CardExpense, Category, Card

admin.site.register(Bank)
admin.site.register(Card)
admin.site.register(Category)
admin.site.register(BankExpense)
admin.site.register(CardExpense)