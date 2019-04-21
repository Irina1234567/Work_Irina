# Получите текст из файла.

import re

with open('text.txt','r',encoding='utf-8') as f:
    text_1 = f.read()
    print(text_1)

# 2. Разбейте текст на предложения.

print(re.split("\.\s",text_1))


# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.

print(re.split("\s\W", text_1))

li_1 = re.findall("[а-я?А-Я]+",text_1)

print(li_1)

result = [word for word in li_1 if len(word) >= 4]

print(result)

from collections import Counter
words = Counter(result)
print(words)

# 4. Отберите все ссылки.
li_2 = re.findall("\w+@?\w\.\w+",text_1)
print(li_2)


# 5. Ссылки на страницы какого домена встречаются чаще всего?

domens = Counter(li_2)
print(domens)

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

text = re.sub("\w+@?\w\.\w+","Ссылка отобразится после регистрации",text_1)

print(text)

