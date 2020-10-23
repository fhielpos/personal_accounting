from django.db import models
from datetime import date


MONTHS = [
    ('ENE', 'Enero'),
    ('FEB', 'Febrero'),
    ('MAR', 'Marzo'),
    ('ABR', 'Abril'),
    ('MAY', 'Mayo'),
    ('JUN', 'Junio'),
    ('JUL', 'Julio'),
    ('AGO', 'Agosto'),
    ('SEP', 'Septiembre'),
    ('OCT', 'Octubre'),
    ('NOV', 'Noviembre'),
    ('DIC', 'Diciembre'),
    ]

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name

class Expense(models.Model):
    expense_date = models.DateField(default=date.today)
    ammount = models.FloatField()
    expense_type = models.OneToOneField(Category, verbose_name="Expense category", on_delete=models.CASCADE)
    
    def __str__(self):
        expense_str = str(self.expense_type) + ": $ " + str(self.ammount)
        return expense_str

class CreditBalance(models.Model):
    month = models.CharField(max_length=3, choices=MONTHS)
    credit_expenses = models.ManyToManyField(Expense, verbose_name="List of expenses")
    balance = models.FloatField()
    
    def __str__(self):
        return self.balance

class Bank(models.Model):
    bank_name = models.CharField(max_length=20)
    balance = models.FloatField()

    def __str__(self):
        return self.bank_name

class Card(models.Model):
    card_name = models.CharField(max_length=20)
    card_balance = models.FloatField(default=0)
    card_bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        card_str = self.card_name +" " +str(self.card_bank)
        return card_str

class CardExpense(Expense):
    expense_card = models.ForeignKey(Card, on_delete=models.CASCADE)

class BankExpense(Expense):
    expense_bank = models.ForeignKey(Bank, on_delete=models.CASCADE)