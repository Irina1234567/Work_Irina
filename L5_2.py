# Создайте модуль.
# В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random
print ("Введите список чисел через пробелы, в конце нажмите Enter")
def randomlist ():
    list1 = [int(i) for i in input().split()]
    if not list1: 
        return None
    else:
        d = random.choice(list1)
        return d
print (randomlist())