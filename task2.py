def ans(n):
    if n in(12, 1, 2):
            return 'зима'
    if n in(3, 4, 5):
            return 'весна'
    if n in(6, 7, 8):
            return 'лето'
    if n in(9, 10, 11):
            return 'осень'
    return 'Ошибка'


print(ans(int(input())))
