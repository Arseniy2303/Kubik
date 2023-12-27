color = int(input('Введите длину волны'))
while True:
    color = int(color)
    if (color>=380) and (color<450):
        print('Цвет волны - фиолетовый')
    elif (color>=450) and (color<495):
        print('Цвет волны - синий')
    elif (color>=495) and (color<570):
        print('Цвет волны - зелёный')
    elif (color>=570) and (color<590):
        print('Цвет волны - жёлтый')
    elif (color>=590) and (color<620):
        print('Цвет волны - оранжевый')
    elif (color>=620) and (color<=750):
        print('Цвет волны - красный')
    else:
        print('Не могу сказать цвет волны')
    print('Введите длину волны или "enter" для выхода.')
    color = input()
    if color == '':
        break