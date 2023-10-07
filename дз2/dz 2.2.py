spisok = []
while True:
    element = input("Введите элемент списка(для завершения введите пустую строку):")
    if not element:
        break
    spisok.append(element)
spisok = sorted(spisok, reverse=True)
max_number = "".join(spisok)
print("Максимальное число: ", max_number)
