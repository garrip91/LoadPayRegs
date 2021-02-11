import openpyxl
from pathlib import Path
from LoadPayRegsProject.settings import MEDIA_ROOT

from .models import TableAndUrlColumns
from django.db.models import Sum

def read_doc(xlsx_file_path):
    #full_path = Path('/media/docs') / xlsx_file_path
    #wb = openpyxl.load_workbook(full_path)
    #print(str(full_path))
    wb = openpyxl.load_workbook(xlsx_file_path)
    sh = wb.active
    print(sh['b4'].value)
    # ...дальше необходимо прикрутить сюда цикл

def total_result():
    result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=False).aggregate(Sum('accounts_amount'))
    result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=False).aggregate(Sum('payment_balance'))
    return (result1['accounts_amount__sum'], result2['payment_balance__sum'])