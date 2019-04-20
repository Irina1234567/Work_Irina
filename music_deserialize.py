#2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию.import pickle

import json
import pickle


json_to_dict = json.load(open('group.json', 'r'))
print(json_to_dict)


pickle_to_dict = pickle.load(open('group.pickle', 'rb'))
print(pickle_to_dict)

