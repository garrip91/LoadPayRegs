from django.db.models import Sum

@property
def total_result(self):
    total_result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=True).aggregate(Sum('accounts_amount'))
    total_result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=True).aggregate(Sum('payment_balance'))
    return (result_sum1, result_sum2)
    
print(total_result)