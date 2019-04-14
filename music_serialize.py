# Работа с файлами
# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {
    'name': 'Beatls',
    'tracks': ['Yellow Submarine', 'Yearsteday','Abbey Road','Dig It','Let it Be','Misery'],
    'Albums': [
        {'name': 'Let it Be','year': 1970},
        {'name': 'Abbey Road','year': 1969},
        {'name': 'Please Please Me}','year': 1963}
    ]
}

dict_to_json = json.dumps(my_favourite_group)
print(dict_to_json)

dict_to_pickle = pickle.dumps(my_favourite_group)
print(dict_to_pickle)

with open('group.json', 'w', encoding='utf8') as f:
    f.write(dict_to_json)

with open('group.pickle', 'wb',) as f:
        f.write(dict_to_pickle)