#import collections
from collections import defaultdict #Используем подкласс dict модуля collection, т.е. тоже словарь
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
#my_analys = {} #Использование простого словаря не даст возможность добавить значение. Выведет только последний ввод
my_analys = defaultdict(list) #Это чтобы потом использовать метод append, добавления в конец списка значения
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    my_analys['название'].append(my_dict.get('название'))
    my_analys['цена'].append(my_dict.get('цена'))
    my_analys['количество'].append(my_dict.get('количество'))
    my_analys['ед'].append(my_dict.get('ед'))
    n += 1
print(my_list)
print(dict(my_analys)) #Обратно переводим в обычный словарь, чтобы в выводе убрать тип defaultdict и др. интересно, а если словарь большой будет
#print(dict.__repr__(my_analys))
