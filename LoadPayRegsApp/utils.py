from .models import TableAndUrlColumns
from django.db.models import Sum

def total_result():
    result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=False).aggregate(Sum('accounts_amount'))
    result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=False).aggregate(Sum('payment_balance'))
    return (result1['accounts_amount__sum'], result2['payment_balance__sum'])