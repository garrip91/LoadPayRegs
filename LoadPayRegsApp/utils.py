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
    #sh = wb.active
    sheets = wb.sheetnames
    sheet = wb[sheets[0]]
    #print(sh['b4'].value)
    column = sheet['A'][3:-1]
    A_list = []
    #A_dict = {}
    for cell in column:
        #print(type(cell.value))
        #print(cell.value)
        A_list.append(cell.value)
    print(A_list)
    #A_dict = dict(enumerate(A_list))
    #print(A_dict)
    #print(xlsx_file_path)
    # ...дальше необходимо прикрутить сюда цикл
    return A_list

def total_result():
    result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=False).aggregate(Sum('accounts_amount'))
    result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=False).aggregate(Sum('payment_balance'))
    return (result1['accounts_amount__sum'], result2['payment_balance__sum'])