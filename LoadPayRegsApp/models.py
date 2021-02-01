from django.db import models

# Create your models here:

class Document(models.Model):
    docfile = models.FileField(upload_to='docs/')

class TableColumns(models.Model):
    organization
    material_assigning
    account_purpose
    contract_number
    contract_amount
    paid1
    account_number
    account_date
    accounts_amount
    for_payment
    payment_balance
    paid2
    remainder
    note
    result_sum1
    result_sum2