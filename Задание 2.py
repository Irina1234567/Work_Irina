# Задание 2
number = int(input('введите число:'))
while number >= 0 and number <= 10:
    number = number ** 2
    print(number)
    break
else:
    print('не верно. ведите числов диапазоне от 0 до 10')