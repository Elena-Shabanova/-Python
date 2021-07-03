srtroka = input('Введите строку, разделяя слова пробелами: ').split()
text1 = '-элемент строки : '
text2 = '-элемент строки, первые 10 символов : '
for j in range(len(srtroka)):
    if len(srtroka[j])<=10: #Проверка длины слова
        print(j+1, text1, srtroka[j]) #Вывод всего короткого слова
    else:
        srtroka10 = srtroka[j] #Сохранение длинного слова в отдельной переменной
        print(j + 1, text2, srtroka10[:10]) #Вывод первых 10 символов слова
