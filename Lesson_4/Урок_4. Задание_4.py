# 4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр –
# armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# 1. Наносит урон. Это улучшенная версия функции из задачи 3.
# 2. Вычисляет урон по отношению к броне.
# Примечание.
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

import random

player = {'player': input('Введите имя игрока:'),
          'health': random.randint(50, 100),
          'damage': random.randint(25, 50),
           'armor': 1.2}

enemy = {'player': input('Введите имя врага:'),
         'health': random.randint(50, 100),
         'damage': random.randint(25, 50),
          'armor': 1.2}

print('Создан игрок: ', player)
print('Создан враг: ', enemy)


def attack_armor(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage'] / person1['armor'])})
    # print('attack_armor', person2['player'], person2['health'])
    return person2['damage']

def damage_armor(person1):
    person1.update({'armor': round(person1['armor'] - random.uniform(0, 0.1), 1)})
    if person1['armor'] < 1:
        person1.update({'armor': 1})

    return person1['armor']


def game2(step=1):
    step1 = step
    while step > 0:
        xwho = bool(random.getrandbits(1))
        print('Шаг {}'.format(step1 - (step - 1)))
        if xwho:

            if player['armor'] > 1:
                damage_armor(player)

            else:
                attack_armor(enemy, player)
            print('Нанесён урон игроку {} : {} {} {}'
                  .format(player['player'], player['health'],
                          player['armor'], player['damage']))

        else:
            if enemy['armor'] > 1:
                damage_armor(enemy)

            else:
                attack_armor(player, enemy)
            print('Нанесён урон врагу {} : {} {} {}'
                  .format(enemy['player'], enemy['health'],
                          enemy['armor'], enemy['damage']))

        if player['health'] <= 0 or enemy['health'] <= 0:
            print('Игра окончена')
            if player['health'] > enemy['health']:
                print('Победил игрок, :), здоровье {}'.format(player['health']))
            elif enemy['health'] > player['health']:
                print('Победил враг, Ж(, здоровье {}'.format(enemy['health']))
            elif enemy['health'] == player['health']:
                print('Ничья, игрок {}, враг {}'.format(player['health'], enemy['health']))
            break
        step -= 1

game2(100)

