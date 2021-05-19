name = input('Введите Ваше имя: ')
voz = int(input('Введите Ваш возраст: '))
rost = float(input('Введите Ваш рост в метрах: '))
ves = float(input('Введите Ваш вес в килограммах: '))
IMT = ves/rost**2
text = name+', '+str(voz)+' год, вес '
text2 = ' ИМТ='+str(IMT)+' - займитесь собой! '
if 0<voz<=21:
        print ('Привет, ', name, ',', 'твой индекс массы тела равен ', int(IMT))
else:
    print('Здравсвуйте, ', text, 'Ваш индекс массы тела равен ', int(IMT))
    print("Уважаемый(ая) {0}, Ваш {1}".format(name, text2))