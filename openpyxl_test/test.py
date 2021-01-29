import openpyxl

# Читаем excel-файл:
wb = openpyxl.load_workbook('reestr_podryadchiki.xlsx')

# ====== Печатаем список листов: ====== #
# sheets = wb.sheetnames
# for sheet in sheets:
    # print(sheet)
    
# ====== Получаем активный лист: ====== #
sheet = wb.active
print(sheet)

# ====== Печатаем тип и значение содержимого ячейки: ====== #
print(type(sheet['J5'].value))
print(sheet['J5'].value)

# ====== Выводим значения всех ячеек активного листа: ====== #
# for row in sheet.rows:
    # string = ''
    # for cell in row:
        # string = string + str(cell.value) + ' '
    # print(string)