import openpyxl
from pathlib import Path
from LoadPayRegsProject.settings import MEDIA_ROOT

from .models import TableAndUrlColumns
from django.db.models import Sum

def read_doc(xlsx_file_path):
    wb = openpyxl.load_workbook(xlsx_file_path)
    sheets = wb.sheetnames
    sheet = wb[sheets[0]]
    column = sheet['A'][3:-1]
    A_list = []
    for cell in column:
        A_list.append(cell.value)
    #print(A_list)
    return A_list

def total_result():
    result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=False).aggregate(Sum('accounts_amount'))
    result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=False).aggregate(Sum('payment_balance'))
    return (result1['accounts_amount__sum'], result2['payment_balance__sum'])