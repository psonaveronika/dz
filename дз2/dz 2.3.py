n = int(input("Введите число: "))
for i in range(1, n + 1):
    print(" " * ((n + 1) - i - 1) + "*" * (2 * i - 1))
