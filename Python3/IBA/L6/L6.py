print('Task #1')
print('Работа с исключениями')
try:
    number1 = 1
    number2 = 2
    print("Результат деления:", number1/number2)
except ValueError:
    print('Невозможно преобразовать в тип int')
except ZeroDivisionError:
    print('Деление на ноль')
except Exception:
    print("Что то пошло не так")
finally:
    print('Деление выполнено успешно')


print('\nРабота с файлами:\n')
print('Task #2.1')
FILENAME = 'L6 - Task_2.txt'
#body = '''Владей собой среди толпы смятенной,
#Тебя клянущей за смятенье всех,
#Верь сам в себя, наперекор вселенной,
#И маловерным отпусти их грех;'''

#with open(FILENAME, 'a') as file:
#    file.write(body)
sp = []
with open(FILENAME, 'r') as file:
    for line in file:
        print(line, end='')
        sp.append(line)


print('''\n
Task #2.2
Считайте весь файл text.txt в список строк, выведите только 
1-ю и последнюю строки:''')
print(sp[0], sp[len(sp)-1])


print('''\n
Task #2.3
Создайте файл chisla.txt содержащий произвольные натуральные
числа, выведите количество этих чисел, их сумму и максимальное 
число''')
FILENAME = 'L6 - chisla.txt'
import random

i = random.randrange(2, 15)
print('i = ', i)

with open(FILENAME, 'w') as file:
    k = 0
    while (k < i):
        file.write(str(random.randint(1,33)) + '\n')
        k+=1

print('Полученные числа:')
with open(FILENAME, 'r') as file:
    for line in file:
        print(line, end='')

spec = []
with open(FILENAME, 'r') as file:
    for line in file:
        spec.append(int(line))
        
print('Количество чисел:', len(spec))
print('Сумма чисел:', sum(spec))
print('Максимальное число:', max(spec))


print('''\n
Task #3.1
Из файла с именем "L6 - color_list.csv" выведите
• все данные в консоль;
• выведите в консоль только названия цветов.''')

FILENAME = "L6 - color_list.csv"

import csv

with open(FILENAME, 'r', newline='') as file:
    reader = csv.DictReader(file)
    print('Вывод всех данных в консоль:')
    for row in reader:
        print(row['color'], ':', row['code'])

with open(FILENAME, 'r', newline='') as file:
    reader = csv.DictReader(file)
    print('Вывод в консоль только названий цветов:')
    for row in reader:
        print(row["color"], end=' ')


print('''
Task #3.2
Из файла с именем "L6 - color_list.csv":
• прочитайте только названия цветов и 
запишите их в список;
• запишите список с названиями цветов в 
новый текстовый файл "L6 - color_list.txt";
• проверьте наличие созданного файла;
• если в файле одна строка, сделайте каждый 
цвет с новой строки.''')

spis = []
with open(FILENAME, 'r', newline = '') as file:
    reader = csv.DictReader(file)
    for row in reader:
        spis.append(row['color'])
print(spis)


FILENAME_2 = 'L6 - color_list.txt'
with open(FILENAME_2, 'w') as file:
    for i in spis:
        file.write(i + ' ')
    print('Список цветов записан в файл', FILENAME_2)


try:
    file = open(FILENAME_2)
except IOError as e:
    print(u'не удалось открыть файл')
else:
    with file:
        print('Файл успешно создан')
        file.close()

spis_ch = []
with open(FILENAME_2, 'r') as file:
    for line in file:
        spis_ch.append(line)
if len(spis_ch) == 1:
    print("Длина списка = 1")
    with open(FILENAME_2, 'w') as file:
        for i in spis:
            file.write(i + '\n')
    print('Каждый цвет записан в новой строке в файле:', FILENAME_2)
    with open(FILENAME_2, 'r') as file:
        for line in file:
            print(line, end='')
else:
    print('Цвета изначально записывались как надо')