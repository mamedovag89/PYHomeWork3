# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
def List (size, min, max):
    list =[]
    for i in range(size):
        list.append(random.uniform(min, max))
    return list
print (' Введите количество элементов списка: ')
size_list = int(input())
print (' Введите min возможное  числа в  списке: ')
min_num = int(input())
print (' Введите max возможное  числа в  списке: ')
max_num = int(input())

new_list = List(size_list, min_num, max_num)
result_list = []
for i in new_list:
    if i - int(i) !=0:
        result_list.append(abs(i - int(i)))
        min_num = min(result_list)
        max_num = max(result_list)
print (f' Для списка {new_list} разница между max и min значение дробной части равна{max_num - min_num} ')        

