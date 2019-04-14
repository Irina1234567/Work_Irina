# Решить с помощью генераторов списка.
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

list_1 = ['банан', 'груша', 'яблоко', 'апельсин', 'киви', 'mango']
list_2 = ['mango', 'вишня', 'киви', 'банан', 'персик', 'хурма', 'слива']

sp_result = [i for i in set(list_1) if i in set(list_2)]

print ("Список 1 - " + str(list_1))
print ('Список 2 - ' + str(list_2))
print ('Присутствуют в обоих - ' + str(sp_result))
