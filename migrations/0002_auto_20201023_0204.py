# Generated by Django 3.1.2 on 2020-10-23 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_accounting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='month',
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_balance',
            field=models.FloatField(default=0),
        ),
    ]
