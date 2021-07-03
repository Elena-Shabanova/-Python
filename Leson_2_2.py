list_my=input('Введите элементы списка (символы, текст или числа): ').split() # Работает с четным и нечетным количеством эл-тов

for j in range(0, len(list_my)-1, 2):
    list_my[j], list_my[j+1] = list_my[j+1], list_my[j]

print('Элементы списка поменялись местами: ', list_my)

