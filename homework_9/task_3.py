# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open(r'test_file/task_3.txt', encoding='utf-8') as incoming:
    k = [[]]
    for line in incoming.readlines():
        if line == '\n':
            k.append([])
        else:
            k[-1].append(int(line))

for i, j in enumerate(k):
    k[i] = sum(j)

three_most_expensive_purchases = sum(sorted(k)[-3:])

assert three_most_expensive_purchases == 202346
