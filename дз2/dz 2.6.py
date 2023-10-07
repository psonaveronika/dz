str = input("Введите строку: ")
k = int(input("Введите число k: "))
count = 0
for char in str:
    if char.isdigit():
        count += 1
        if count == k:
            print("k-ая цифра:", char)
if count < k:
    print("Ошибка: k превышает длину строки")
