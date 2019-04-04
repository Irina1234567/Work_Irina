 # Задание 3 "Медицинская анкета"
name = input('Введите имя и фамилию ')
age = int(input('Введите возраст '))
weigh = int(input('Введите вес '))
if age < 30 and  (50 <= weigh <= 120):
    print(name,age,weigh,'— хорошее состояние.')
elif age > 30 and  (weigh >= 120 or weigh <= 50):
    print(name, age, weigh,'— следует заняться собой.')
elif age > 40 and (weigh >= 120 or weigh <= 50):
    print(name,age,weigh,'—  требуется врачебный осмотр')
else:
    print(name,age,weigh,'— продолжайте следить за собой!')
