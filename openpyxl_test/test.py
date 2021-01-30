import openpyxl

# Читаем excel-файл:
wb = openpyxl.load_workbook('reestr_podryadchiki.xlsx')

sheets = wb.sheetnames

# ====== Получаем нужный нам лист по индексу: ====== #
sheet = wb[sheets[0]]

# ====== Печатаем список листов: ====== #
# for sheet in sheets:
    # print(sheet)
    
# ====== Получаем активный лист: ====== #
# sheet = wb.active
# print(sheet)


# ====== Печатаем нужный нам лист: ====== #
# print(sheet)

# ====== Печатаем тип и значение содержимого ячейки: ====== #
# print(type(sheet['J28'].value))
# print(sheet['J28'].value)

# ====== Проходим циклом по типам и значениям содержимых нужной нам колонки (колонки - латинские буквы, строки - числа): ====== #
# n = 1
# while n <= 36:
    # print(type(sheet[f'H{n}'].value))
    # print(sheet[f'H{n}'].value)
    # n += 1
column_h = sheet['H']
for cell in column_h:
    print(type(cell.value))
    print(cell.value)

# ====== Выводим значения всех ячеек активного листа: ====== #
# for row in sheet.rows:
    # string = ''
    # for cell in row:
        # string = string + str(cell.value) + ' '
    # print(string)