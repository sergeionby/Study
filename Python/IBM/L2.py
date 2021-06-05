#type() - функция, определяющая тип пременной

score1 = 50.5648
score2 = 23.5501
score3 = 96.560

#Задание 1.1 - Разделить два целых числа, вывести: 
#- результат деления и его тип 
#- округлить ответ до 2-ух знаков после запятой
print('\n'+'Задание 1.1')
a=int(score1)/int(score2)
print(a, type(a))
print(round(a, 3))
print(round(a, 2))

#Задание 1.2 - Вывести округленные числа
print('\n'+'Задание 1.2')
print(round(score1), round(score2), round(score3), sep='--')

#Работа со строками
print('\n'+'Работа со строками')
word='Python'
print(word)
print('character in position  0: '+word[0])
print('character in position  5: '+word[5])
print('character in position -1: '+word[-1])
print('character in position -2: '+word[-2])
print('characters in position 0-2: '+word[:2])
print('characters in position 2:5: '+word[2:5])
print('character in positions from 4: '+word[4:])
word_2='J'+word[1:]
print('Summ str:', word_2)

#Задание 2 - Спросить у пользователя его имя и фамилию:
#1) вывести имя и фамилию с заглавных букв;
#2) вывести имя и фамилию в верхнем регистре;
#3) вывести инициалы (например, О.В.);
#4) вывести длину строки (имя + фамилия)
print('\n'+'Задание 2')
n=input('Input your name: ')
f=input('Input your surname: ') 
print('1) ', n.capitalize(), f.capitalize())
print('2) ', n.upper(), f.upper())
print('3) ', n[0].upper()+'.'+f[0].upper()+'.')
print('4) ', len(n+f))

#Задание 3.1
print('\n'+'Задание 3.1')
print('Задание: проверить исло на четность')
a=input('Введите число: ')
if int(a)%2 == 0 : print('Ваше число четное')
else : print('Ваше число нечетное')

#Задание 3.2
print('\n'+'Задание 3.2')
print('''Написать диалог с пользователем: "какая сегодня погода(ясно,
дождливо, ветрено)". В зависимости от выбранного ответа вывести
сообщение: "возьми зонтик" "не забудь панаму" и т. д.
''')
za_oknom = input('какая сегодня погода(ясно, дождливо, ветрено)? ')
if za_oknom == 'ясно' : print('не забудь панаму')
elif za_oknom == 'дождливо' : print('возьми зонтик')
elif za_oknom == 'ветрено' : print('одень куртку')
else : print('непонятно, поэтому останьтесь дома')

#Задание 4
print('\n'+'Задание 4')
print(''' Даны a, b, k, m. Вычислить С''')
import math
a=3
b=1
k=1
m=2
c=math.sqrt((a-b)**2/abs(k-m))
print('a =', a, 'b =', b, 'k =', k, 'm =', m, '\n', c)