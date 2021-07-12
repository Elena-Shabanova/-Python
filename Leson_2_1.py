#a = input('Введите элементы списка: ')
a = ['g', 5, 10.5, complex(2,7), True, None, ('zima', 1), {'январь': 1, 'декабрь': 12}]
print(a)
j = 0
for i in a:
    print("{} {}-й эл-т списка имеет тип: {})".format(i, j, type(i))) # Длинный вариант вывода
    j +=1

#for i in a:
   # print(f'{i} is {type(i)}') # Короткий вариант вывода