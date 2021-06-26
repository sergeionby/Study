print('''Task 1.1
Исправте ошибки в коде из слайда''')

oklad=100#int(input("Оклад: "))
procent=3#int(input("% налога: "))
nalog=oklad*procent/100
summa=oklad-nalog
print ("Сумма на руки:",summa)
print ("Налог:",nalog)


print('''\nTask 1.2
Определить возраст по дате рождения.
Наряду с блок схемами использую словесное описание алгоритма:
1. Ввести текущую дату
2. Ввести дату рождения
3. Найти возраст = текущая дата – дата рождения''')

from datetime import datetime

#bithday = datetime.strptime(input('Введите дату рождения в формате ДД.ММ.ГГГГ: '), '%d.%m.%Y')
bithday = datetime(2000, 1, 1, 0,0,0)
age = datetime.today() - bithday
print('Вам сейчас:', int(age.days/365))


print('''
Task #1.3
Введите с клавиатуры дату рождения.
Выведите день недели и месяц дня рождения.''')

from datetime import date

bithday = date(2000, 1, 1)
print(bithday, '-->', bithday.strftime('%A, %B'))


print('''
Task 2.1
Можно ли из бревна, имеющего диаметр поперечного сечения 
D, выпилить квадратный брус шириной А?''')

import math

d = 5
a = 5

if d*math.sqrt(2)/2 >= a:
    print('Yes')
else:
    print('No')



print('''
Task 2.2
В csv-файле содержаться записи температуры воздуха в различных городах 
(допустим сводка погоды), необходимо прочитать данные из файла и по 
названию города, введенного с клавиатуры, вывести сообщение 
«Сейчас в Питере жарко». Критерий оценки:
если t<18 – «холодно»,
если 18<t<26 – «комфортно»,
если t>26 – «жарко».\n''')

import csv

FILENAME = 'L7 - Temp.csv'
#city = 'Минск'
city = input('Введите название города с заглавной буквы: ')

with open(FILENAME, 'r', newline='', encoding='utf8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for i in row.values():
            if i == city:
                print(row)
                temp = int(row.get('temp'))
                pr = 'Сейчас в г.{0} {1}'
                if temp <= 15 :
                    print(pr.format(row['city'], 'холодно'))
                elif temp > 15 and temp < 26:
                     print(pr.format(row['city'], 'комфортно'))
                elif temp >= 26 :
                    print(pr.format(row['city'], 'жарко'))


print('''
Task 3.1
Пользователь вводит с клавиатуры N чисел.
Используя метод строки format() реализовать следующий вывод:
«Сумма введенных чисел: . Минимальное значение: . Максимальное значение: »''')

n = 3 #int(input('Введите количество чисел: '))
spis = []
for i in range(n):
    spis.append(i) #int(input('Введите число: ')))
print(spis)
vivod = 'Сумма введенных чисел: {0}. Минимальное значение: {1}. Максимальное значение: {2}.'
print(vivod.format(sum(spis), min(spis), max(spis)))


print('''
Task 3.2
Пользователь вводит любую дату и получает день недели до тех пор,
пока вводит «да» на вопрос «Хотите продолжить? да/нет».
Вывод ответа должен быть организован в формате:
"2021 Jun 18 was a Fridaу"''')

from datetime import date

answer = 'да'
while answer == 'да':
    #d = datetime.strptime(input('Введите дату в формате ДД.ММ.ГГГГ: '), '%d.%m.%Y')
    d = datetime.strptime('25.06.2021', '%d.%m.%Y')
    print(d.strftime('%Y %b %d was a %A'))
    answer = input('Хотите продолжить? да/нет: ')


print('\nСортировка пузырьковым методом:')
#создаем список
li = [0, 5, 8, 4, 9, 3]
#вычисляем длину списка
n = len(li)
#внешний цикл отсчитывает количество "проходов" по списку
for j in range(0,n-1):
#вложенный цикл сравнивает i-ый c i+1 элементом и при необходимости меняет их местами
#количество сравнений каждый раз уменьшается на величину j
    for i in range(0,n-j-1):
        if li[i] > li[i+1]: #">" сортиует по возрастанию, "<" сортирует по убыванию
            li[i],li[i + 1] = li[i + 1], li[i]
    print(j+1, "- ый проход цикла -> ",end=" ")
    print(li)
print(li)
