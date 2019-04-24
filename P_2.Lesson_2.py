# 1. Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений,

import re
with open('Index.html',encoding='utf-8')as f:
    text_1 = f.read()

li_1 = re.findall("Нас уже (.*?) человек",text_1)
print(li_1)



# b) при помощи библиотеки BeautifulSoup

from bs4 import BeautifulSoup as BS
soup = BS (text_1,"html.parser")
#print(soup.prettify())
#text_2 = soup.find("""Нас уже() человек""")
# text_2 = soup.find(align="center")
# print(text_2)
 
