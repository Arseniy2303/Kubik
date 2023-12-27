def function(a):
    if a == 1:
        return "Первый"
    elif a == 2:
        return "Второй"
    elif a == 3:
        return "Третий"
    elif a == 4:
        return "Четвертый"
    elif a == 5:
        return "Пятый"
    elif a == 6:
        return "Шестой"
    elif a == 7:
        return "Седьмой"
    elif a == 8:
        return "Восьмой"
    elif a == 9:
        return "Девятый"
    elif a == 10:
        return "Десятый"
    elif a == 11:
        return "Одиннадцатый"
    elif a == 12:
        return "Двенадцатый"
    else :
        return "Неверное число"
a = int(input("Введите число: "))
print(function(a))