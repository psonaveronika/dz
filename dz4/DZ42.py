def factorial(n):
    # базовый случай: факториал 0 равен 1
    if n == 0:
        return 1
    # рекурсивный случай: вычисляем факториал для числа n-1 и умножаем на текущее число n
    return n * factorial(n-1)

n = int(input("Введите число: "))
result = factorial(n)
print(f"{n}! = {result}")
