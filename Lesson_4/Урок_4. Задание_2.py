#2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

def max_numbers(a,b,c):
    numbers_list = [a, b, c]
    max_number = (max(numbers_list))
    return max_number

result = max_numbers(a,b,c)
print('Наибольшее число {}'.format(result))