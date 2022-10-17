from ast import If
import numbers
import time

# Знакомство с языком Python (семинары)
# Урок 2. Знакомство с Python. Продолжение

# Задача 1. 
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задача 1')
def multiplicationNumbers(number):
    print(number)
    numbers = []
    multiplication = 1
    count = multiplication
    for i in range(number):
        multiplication = count * multiplication
        numbers.append(multiplication)
        count += 1
    print(numbers, end=' ')

multiplicationNumbers(4)
print()
multiplicationNumbers(5)
print()


# Задача 2.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ.
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

print('Задача 2')
n = int(input('Введите число N: '))
numbersN = []
indexN = []
multiplicationN = 1
for i in range(-n, n+1, 1):
    numbersN.append(i)
print(numbersN)

for i in input('Введите номер индекса: ').split():
    indexN.append(int(i))

for i in range(len(indexN)):
    multiplicationN = multiplicationN * indexN[i]
print(f'Произведение элементов {multiplicationN}')


# Задача 3. Минимальный делитель
'''
Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
Пример: N = 15: ответ: 3; N = 35: ответ: 5
№	INPUT.TXT	OUTPUT.TXT
'''
# 1 способ
n = int(input('Введите целое число N: '))
division = 2
while n % division != 0:
    division += 1
print(division)

# 2 способ
n = int(input('Введите целое число N: '))
division = 2 # делитель
for i in range(1, int(n)):
    while (n % division == 0):
        print("{:5d}|{:<6d}".format(round(n), division))
        n = n / division
    division += 1
print("{:5d}|".format(round(n)))


# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
print('Задача 4')
def sumNumbers(number):
    print('Чётные числа:')
    sum = 0
    i = 1
    while i <= number:
        if i % 2 == 0:
            sum = sum + i
            print(i)
        i = i + 1
    print('Сумма чётных чисел, sum = ', sum)
sumNumbers(12)
sumNumbers(5)


'''
#  ДОПОЛНИТЕЛЬНАЯ ЗАДАЧА => МОНЕТКИ
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Монетки
    Входные данные: писаны натуральные числа N (1 ≤ N ≤ 100) – число монеток. В каждой из последующих N строк 
                    содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.
    Выходные данные: выведите минимальное количество монет, которые нужно перевернуть.
Пример
№	INPUT.TXT   МОНЕТЫ	OUTPUT.TXT
1	    5
                   1
                   0
                   1
                   1
                   0
                            2
'''
from random import randint
countN = int(input("Введите число монеток: "))
tails = 0
emblem = 0
count = 0
for i in range(countN):
    x = randint(0, 1)
    if x == 0:
        emblem += 1
    else:
        tails += 1
    print(x)
if emblem >= tails:
    count = countN - emblem
else:
    count = countN - tails
print('Минимальное количество монет, которые нужно перевернуть:', count)


#  ДОПОЛНИТЕЛЬНАЯ ЗАДАЧА => ШЕРЕНГА
'''
Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, 
в порядке невозрастания.
Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
чтобы не нарушить традицию, если заранее известен рост каждого ученика и 
эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). 
Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.
    Входные данные: первая строка содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю).
                    Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания.
                    Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.
    Выходные данные: выведите единственное целое число – номер Пети в шеренге учеников.
Пример
№	INPUT.TXT	                        OUTPUT.TXT
1	    8
    165 163 160 160 157 157 155 154
    162	                                    3
'''
heightStudents = [165, 163, 160, 160, 157, 157, 155, 154]
print(heightStudents)
countN = int(input('Введите рост ученика:'))
placeLine = 0
for i in range(len(heightStudents)):
    if heightStudents[i] <= countN and heightStudents[placeLine] >= countN:
        placeLine = i + 1
print(placeLine)
