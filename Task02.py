# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def par(list):
    listnew = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        listnew.append(list[i]*list[count])
        count -= 1
        i += 1
    return listnew
list = [2, 3, 4, 5, 6]
listnew = par(list)
print(list)
print(listnew)