# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from re import A


n = int(input('Введите число: '))
a = ''

while n > 0:
    a = str(n % 2) + a 
    n = n // 2
print(a)