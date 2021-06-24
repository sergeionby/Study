#Задание 1.1
print("Используя кортеж подсчитать количество букв в четверостишье:")
st='''У Марфы на кухне
Cтояло лукошко,
В котором дремала
Домашняя кошка.'''
print('"' + st + '"')
tuple(st)
o=0
l=0

for i in st:
    if i == 'о'  or i == 'О': o+=1
    if i == 'л'  or i == 'Л': l+=1
print("Количество 'о':", o)
print("Количество 'л':", l)
print("Количество 'ш':", st.count('ш')+st.count('Ш'))


#Task 1.2
print('\n'+'Дана некоторая коллекция температур по дням. Допишите скрипт для расчета средней температуры.')
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(week_temp)
print("Средняя температура =", int(mean_temp))


#Task 2.1
print('\n' + 'Создайте словарь, содержащий фамилии и номера удостоверений.')

bd = {1:'qwe', 2:'asd', 3:'zcc', 4:'QWE', 5:'DGHGD'}
print('2.1-1 Словарь:', bd)

k=3
print('2.1-2 Значение по ключу', k, '-->', bd.get(k, "Не найдено"))

k=99
print('2.1-2 Значение по ключу', k, '-->', bd.get(k, "Не найдено"))

new={88:'zfhghknfkn'}
bd.update(new)
print('2.1-3 Добавление в словарь нового элемента \n', bd)

print('2.1-4 Размер словоря  -->', len(bd))

new_bd = dict.fromkeys([11,22,3])
print('2.1-5 Новый словарь --> \n', new_bd)

bd |= new_bd
print('2.1-6 Объединение словарей --> \n', bd)

print('2.1-7 Вывести из словаря только фамилии:')
for i in bd.values():
    print(i, end = ' ')
print('\n')


#Task 2.2
print('2.2 Исправить ошибки в коде, требуемый вывод: True')
d1 = {"a": 100, "b": 200, "c":300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(d1.get("b") == d2.get("b"), '\n')


#Task 3.1
print('3.1 Используйте правильный метод, чтобы добавить несколько предметов (more_fruits) в набор фруктов.')
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", 'banana', "grapes"]

for i in more_fruits :
    fruits.add(i)
for i in fruits :
    print(i)


#Task 3.2
print('''3.2 Используя модуль random и оператор while
сгенерируйте 2 множества из 10-ти случайных чисел
в диапазоне от 10 до 30''')
import random
a = set()
b = set()
while len(a) + len(b) < 20:
    if len(a) < 10 : a.add(random.randint(10,30))
    if len(b) < 10 : b.add(random.randint(10,30))

print('a: ', a)
print('b: ', b)

z = a.intersection(b)
print('пересечение множества a и b:', z)

#m = a.difference(b)
m = a.symmetric_difference(b);
print('уникальные элементы (не принадлежащие одновременно a и b):', m)

new_set = a.union(b)
print('объединение множеств a и b:', new_set)
