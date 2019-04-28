#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json

name = input("Ведите название города: ")


link_1 = "http://autocomplete.travelpayouts.com/places2?term="

data_1 = json.loads(requests.get(link_1 + name).text)


print (data_1 [0]["code"])


