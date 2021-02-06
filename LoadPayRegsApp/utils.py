from django.db.models import Sum

@property
def result_sum(self):
    result_sum1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=True).aggregate(Sum('accounts_amount'))
    result_sum2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=True).aggregate(Sum('payment_balance'))
    return (result_sum1, result_sum2)