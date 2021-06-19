#Task 1.1
print('Спросить имяпользователя и вывести приветствие с заглавнойй буквы имени')

def hello(x = "user"):
    print('Hello,' + x.capitalize() + '!')
#name = input('Как вас зовут? ')
#hello(name)
hello('sdf')
hello('1')
hello()


#Task 1.2
print()
print('Написать функцию перевода сумы из BYN в EUR, при этомкурс евро сделать по умочанию')
def kurs(x, eur = 3):
    print(round(x / eur, 2))

kurs(3)
kurs(10)
kurs(20000, 3.5)


#Task 1.3
print()
print('Написать функцию, рассчитывающую сумму любого количества чисел и вызвать её 2-3 раза, указав фактические параметры')

def sum_any(*i):
    print(sum(i))

sum_any(1,1)
sum_any(1,1,1)
sum_any(1,2,3)
sum_any(1,3,55,3,67,11,33,9997,6)


#Task 1.4
print()
print('''Написать функцию, рассчитывающую сумму любого количества чисел
в диапазоне от 0 до N. N вводим с клавиатуры''')
import random
def sum_all(n):
    s=0
    mas = []
    for i in range(0, n+1):
        mas.append(random.randint(1,9))
        s += int(mas[i-1])
    print(mas)
    print(sum(mas))
    
#m = int(input('Введите количество чисел для суммирования: '))
m = 2
if m <= 0 : print(0)
elif m > 0 : sum_all(m)


#Task 2
x = lambda a,b,c : a+b+c
print(x(1,1,1))
print(x(1,2,3))


#Рекурсия

#Task 3.1 
print('\n Дано натуральное число n. Выведите все числа от 1 до n.')
def pr(k):
    if (k>0):
        print(k, end=' ')
        k-=1
        return pr(k)
    else : print('\n end')
pr(3)


#Task 3.2
print('''\n Даны два целых числа A и В (каждое в отдельной строке).
Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания в противном случае.''')
def f(x, y):
    print (x, end=' ')
    if x < y :
        x+=1
        return f(x,y)
    elif x > y :
        x-=1
        return f(x,y)
    else : print('\n end')
a = 5
b = 7
f(a,b)


#Task 3.3
print('''\n Дано натуральное число n>1. Выведите все простые
делители этого числа в порядке возрастания (например, 18 -> 2 3 3).''')
def f2(x,y = [], i=2):
    if (x == 1) : pass
    elif (x%i == 0) :
        x/=i
        y.append(i)
        return f2(x,y,i)
    else:
        i+=1
        return f2(x,y,i)
n = 18
l = []
f2(n,l)
print('Простые множители числа', n, ':')
for i in range(len(l)):
    print (l[i-1], end=' ')
print()

#Task 3.4
print('''\n Дано натуральное число N. Выведите слово YES,
если число N является точной степенью двойки,
или слово NO в противном случае. Операцией возведения в
степень пользоваться нельзя!''')
def f1(x, st = 0):
    if (x <= 1) and (st == 0) : print ('Введенное число -', x)
    elif (x <= 1) and (st > 0) : print('YES')
    elif (x % 2 != 0) : print('NO')
    else:
        x = int(x/2)
        st += 1
        return f1(x, st)
n = 36
f1(n)
