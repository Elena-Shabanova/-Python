#my_list = [8, 1, 3, 5, 3, 7]
my_list = list(input('Введите рейтинг - не возрастающий набор натуральных чисел без пробелов: '))
my_list.append(input('Введите новый элемент рейтинга: '))
#my_list.append(int(input('Введите новый элемент рейтинга: '))) #Добавление нового элемента в конец списка
my_list.sort()#Сортировка измененного списка по возрастанию
my_list.reverse() #Реверс нового списка
#print(", ".join(map(str, my_list)))#Вывод списка без скобок через перевод в строку 1 способ
print(*my_list, sep = ", ")#Вывод списка без скобок через перевод в строку 2 способ