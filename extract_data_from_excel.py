import xlrd3

file = xlrd3.open_workbook('Данные для статобработки.xlsx')  # точка входа в файл
sheet_names = file.sheet_names()  # отображаем название листов экселя
task_1 = file.sheet_by_name(sheet_names[0])  # API для взаимодействия с первым листом эксля

X = [task_1.row_values(row_number)[0] for row_number in range(1, 501)]  # загоняем в список значения X и Y
Y = [task_1.row_values(row_number)[1] for row_number in range(1, 501)]

print(X)
print(Y)
