import openpyxl
from pathlib import Path
# Импорты ниже закомментированы в режиме тестирования:
#from LoadPayRegsProject.settings import MEDIA_ROOT
#from .models import TableAndUrlColumns
#from django.db.models import Sum

def read_doc(xlsx_file_path):
    wb = openpyxl.load_workbook(xlsx_file_path)
    sheets = wb.sheetnames
    ########################################
    # Лист № 1:
    sheet_1 = wb[sheets[0]]
    ##############################
    # Столбец "A":
    column_A = sheet_1['A'][3:-1]
    A_list = []
    for cell in column_A:
        A_list.append(cell.value)
    #print(A_list)
    ##############################
    # Столбец "B":
    column_B = sheet_1['B'][3:-1]
    B_list = []
    for cell in column_B:
        B_list.append(cell.value)
    #print(B_list)
    ##############################
    # Столбец "C":
    column_C = sheet_1['C'][3:-1]
    C_list = []
    for cell in column_C:
        C_list.append(cell.value)
    #print(C_list)
    ##############################
    # Столбец "D":
    column_D = sheet_1['D'][3:-1]
    D_list = []
    for cell in column_D:
        D_list.append(cell.value)
    #print(D_list)
    ##############################
    # Столбец "E":
    column_E = sheet_1['E'][3:-1]
    E_list = []
    for cell in column_E:
        E_list.append(cell.value)
    #print(E_list)
    ##############################
    # Столбец "F":
    column_F = sheet_1['F'][3:-1]
    F_list = []
    for cell in column_F:
        F_list.append(cell.value)
    #print(F_list)
    ##############################
    # Столбец "G":
    column_G = sheet_1['G'][3:-1]
    G_list = []
    for cell in column_G:
        G_list.append(cell.value)
    #print(G_list)
    ##############################
    # Столбец "H":
    column_H = sheet_1['H'][3:-1]
    H_list = []
    for cell in column_H:
        H_list.append(cell.value)
    #print(H_list)
    ##############################
    # Столбец "I":
    column_I = sheet_1['I'][3:-1]
    I_list = []
    for cell in column_I:
        I_list.append(cell.value.strftime('%d.%m.%Y'))
    #print(I_list)
    ##############################
    # Столбец "J":
    column_J = sheet_1['J'][3:-1]
    J_list = []
    for cell in column_J:
        J_list.append(cell.value)
    #print(J_list)
    ##############################
    # Столбец "K":
    column_K = sheet_1['K'][3:-1]
    K_list = []
    for cell in column_K:
        K_list.append(cell.value)
    #print(K_list)
    ##############################
    # Столбец "L":
    column_L = sheet_1['L'][3:-1]
    L_list = []
    for cell in column_L:
        L_list.append(cell.value)
    #print(L_list)
    ##############################
    # Столбец "M":
    column_M = sheet_1['M'][3:-1]
    M_list = []
    for cell in column_M:
        M_list.append(cell.value)
    #print(M_list)
    ##############################
    # Столбец "N":
    column_N = sheet_1['N'][3:-1]
    N_list = []
    for cell in column_N:
        N_list.append(cell.value)
    #print(N_list)
    ##############################
    # Столбец "O":
    column_O = sheet_1['O'][3:-1]
    O_list = []
    for cell in column_O:
        O_list.append(cell.value)
    #print(O_list)
    ########################################
    
    zipped_result = zip(A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list, L_list, M_list, N_list, O_list)
    
    #result = (A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list, L_list, M_list, N_list, O_list)
    
    result = list(zipped_result)

    return result

test = read_doc('contractors_and_suppliers.xlsx')[0]
    
# for i in test:
    # print(type(i))
    # print(i)

# def total_result():
    # result1 = TableAndUrlColumns.objects.filter(accounts_amount__isnull=False).aggregate(Sum('accounts_amount'))
    # result2 = TableAndUrlColumns.objects.filter(payment_balance__isnull=False).aggregate(Sum('payment_balance'))
    # return (result1['accounts_amount__sum'], result2['payment_balance__sum'])
    
def total_result(xlsx_file_path):
    sum1 = 0
    sum2 = 0
    for i in read_doc(xlsx_file_path):
        sum1 += i[9]
        sum2 += i[11]
    result = [sum1, sum2]
    return result
    
print(total_result('contractors_and_suppliers.xlsx')[0])