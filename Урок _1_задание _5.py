revenue = float(input('Введите значение выручки: '))
cost = float(input('Введите значение затрат: '))
text = 'Финансовый результат за отчетный период: '
profit = revenue-cost # Прибыль/убыток
profitability = revenue/cost # Рентабельность
text = 'Финансовый результат за отчетный период: '
if profit >= 0:
        print(text,  "{:2f} руб. прибыль фирмы".format(profit)) 
        print("Рентабельность составила {:05.2f} руб.".format(profitability))
else:
    print(text, "{:2f} руб. убыток фирмы".format(profit))
chtat = float(input('Введите значение затратчисленность сотрудников: '))
print("Прибыль в расчете на 1 сотрудника составила {:05.2f} руб.".format(profit/chtat))
