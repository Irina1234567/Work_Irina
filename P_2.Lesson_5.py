# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.

class Word:
    text = "letter"
    part_of_speech = "Vtor"

    def __init__(self, slovo, chast_r):
        self.text = slovo
        self.part_of_speech = chast_r


s1 = Word ("Поезд", "Podl")
s2 = Word ("мчится", "Skaz")
s3 = Word ("быстро", "Vtr")


print(s1.text)
print(s2.part_of_speech)
print(s3.text)

# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

# word_0 = s1.text + " " + s2.text + " " + s3.text + "!"
# print(word_0)

class Sentence:
    speach = " "
    content = [1, 2, 3]

    def show(self):
        word_1 = self.speach + s1.text + s2.text + s3.text
        print(word_1)

#     def show_parts(self):
#         part_of_speech = self.content
#     print("ЧАСТЬ РЕЧИ"+ part_of_speech)
# table = Sentence()
# print(table.content)
# table.show()
# table.show_parts()
