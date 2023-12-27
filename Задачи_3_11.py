def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    while True:
        try:
            number = int(input("Введите число: "))
            if number < 2:
                print("Число должно быть больше единицы")
                continue
            else:
                result = prime(number)
                print(f"{number} число простое: ", end="")
                if result:
                    print(True)
                else:
                    print(False)
            break
        except ValueError:
            print("Введите допустимое число")


if __name__ == "__main__":
    main()