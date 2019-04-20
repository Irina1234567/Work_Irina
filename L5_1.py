# Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.

import os

def new_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),'dir_' + str(i))
        os.mkdir(new_path)
        print ("Создан каталог "+ new_path)

print (new_dir())

# Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

def del_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),'dir_{}'.format(i))
        os.rmdir(new_path)
        print("Удален каталог " + new_path)

print (del_dir())
