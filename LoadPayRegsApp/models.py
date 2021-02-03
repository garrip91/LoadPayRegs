from django.db import models

from django.db.models import Sum

# Create your models here:
class Document(models.Model):
    docfile = models.FileField(upload_to='docs/')

class TableColumns(models.Model):
    organization = models.CharField(max_length=255, verbose_name="Организация", null=True, blank=True)
    material_assigning = models.CharField(max_length=255, verbose_name="Назначение материала", null=True, blank=True)
    account_purpose = models.CharField(max_length=255, verbose_name="Назначение счёта", null=True, blank=True)
    contract_number = models.CharField(max_length=255, verbose_name="№ договора", null=True, blank=True)
    contract_amount = DecimalField(max_digits=14, decimal_places=2, verbose_name="Сумма по договору", null=True, blank=True)
    paid1 = DecimalField(max_digits=14, decimal_places=2, verbose_name="Оплачено", null=True, blank=True)
    account_number = models.CharField(max_length=255, verbose_name="№ счёта", null=True, blank=True)
    account_date = models.DateField(verbose_name="Дата счёта", null=True, blank=True)
    accounts_amount = DecimalField(max_digits=14, decimal_places=2, verbose_name="Сумма по счётам", null=True, blank=True)
    for_payment = DecimalField(max_digits=14, decimal_places=2, verbose_name="В оплату", null=True, blank=True)
    payment_balance = DecimalField(max_digits=14, decimal_places=2, verbose_name="Остаток по оплате", null=True, blank=True)
    paid2 = DecimalField(max_digits=14, decimal_places=2, verbose_name="Оплачено", null=True, blank=True)
    remainder = DecimalField(max_digits=14, decimal_places=2, verbose_name="Остаток", null=True, blank=True)
    note = models.CharField(max_length=255, verbose_name="Примечание", null=True, blank=True)
    result_sum1 = TableColumns.objects.filter(accounts_amount__isnull=True).aggregate(Sum('accounts_amount'))
    result_sum2 = TableColumns.objects.filter(payment_balance__isnull=True).aggregate(Sum('payment_balance'))