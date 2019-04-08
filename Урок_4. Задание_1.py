
#1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def man_data(name, age, city):
    text = '{},{} год(а),проживает в городе {}'.format(name, age, city)
    return text
name = input('Введите имя ')
age = int(input('Введите возраст '))
city = input('Введите город проживания ')
result = man_data(name, age, city)
print(result)




