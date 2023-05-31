#  Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint
N = 100
x = int(input('Введите число: '))
closeNumber = 1
list = []
for i in range(N):
    list.append(randint(0,100))
print(list)
for number in list:
    if number < x and number > closeNumber:
        closeNumber = number
print(closeNumber)