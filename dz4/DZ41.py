def shifted_lst(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

lst = input("Введите элементы списка через запятую: ").split(',')
k = int(input("Введите число k: "))

print(shifted_lst(lst, k))