# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


import random

player = {'player': input('Введите имя игрока:'),
          'health': random.randint(50, 100),
          'damage': random.randint(25, 50)}

enemy = {'player': input('Введите имя врага:'),
         'health': random.randint(50, 100),
         'damage': random.randint(25, 50)}

print('Создан игрок: ', player)
print('Создан враг: ', enemy)


def attack(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage'])})
    return person2['health']


def game(step=1):
    while step > 0:
        xwho = bool(random.getrandbits(1))
        if xwho:
            attack(enemy, player)
            print('Нанесён урон игроку {} : {}'.format(player['player'], player['health']))
        else:
            attack(player, enemy)
            print('Нанесён урон врагу {} : {}'.format(enemy['player'], enemy['health']))

        if player['health'] <= 0 or enemy['health'] <= 0:
            print('Игра окончена')
            if player['health'] > enemy['health']:
                print('Победил игрок')
            elif enemy['health'] > player['health']:
                print('Победил враг')
            elif enemy['health'] == player['health']:
                print('Ничья')
            break
        step -= 1


game(10)