#Задание 1.1
print('Переменная х изменяется от 1 до 9 с шагом 1.')
print('Вывести значения х, х^2, x^3')
x = 1
while x <= 9:
    print(x, x**2, x**3)
    x+=1
else: ('ready!')

#Задание 1.2
print('\n'+'Проанализировать и исправить ошибку в коде')
х = 5
while x > -5:
    x-=1
    if (x == 0):
        continue
    y=1/x
    print(x, y, sep=" and ")


#Задание 2.1
print('\n' + 'Результаты вывести в одну строку')
for x in 'crocodile':
    if  x == 'd':
        break
    print(x, end = '')

print('\n')
for x in 'banana':
    if x == 'a':
        continue
    print(x, end=' ')

#Задание 2.2
print('\n' +'Вывести числа от 11 до 20 и их квадраты через range()')
for i in range(11, 21):
    print(i, i**2, sep='-->')

#--------
print('\n')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist.index('apple'))
print(thislist.count('apple'))
thislist.reverse()
print(thislist)
thislist.sort()
print(thislist)

print(min(thislist), max(thislist))

s = []
for i in range(5):
    s.append(i**2)
print(s)
l = [x for x in range(10) if x %2 != 0]
print(l)
print('\n')

#Задание 3.1
color = ['Green', 'White', 'Black']
color_ad = ['Red', 'Pink', 'Yellow']
for i in range(len(color_ad)):
 if i==0: color.insert(i, color_ad[i])
 if i==1: color.insert(i+1, color_ad[i])
 if i==2: color.append(color_ad[i])
print('3.1-1: ', color)
print('3.1-2: ', color.sort())
print('3.1-3: ')
for x in color:
    print(len(x), end=', ')
print('\n')

#Задание 3.2
l=[]
for i in range(10, 20):
    l.append(i**2)
print('3.2-1: ', l)

print('3.2-2: ', sum(l))

for r in l:
    if r % 2 ==0: l.remove(r)
print('3.2-3: ', l)

print('3.2-4: ', len(l))


#Задание по желанию
print('\n', 'Пользователь водит большое произвольное число (например, 67548326) и нужно вывести в ответ: в числе 67548326 5 четных и 3 нечетных цифры')
ch = input('Введите произвольное число: ')
c=0
n=0
for i in ch:
    if int(i) % 2 == 0: c+=1
    else n+=1
print('В числе ', ch, c, 'четных и ', n, 'нечетных цифр')
