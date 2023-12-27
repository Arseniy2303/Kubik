def theoremapif(a, b):
    return pow((a*a) + (b*b), 0.5)


a = float(input("Введите длину 1-го катета: "))
b = float(input("Введите длину 2-го катета: "))

c = theoremapif(a,b)
print(f"Длина гипотенузы: {c}")
