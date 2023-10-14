def max_number(spisok):
    max_len = max(len(x) for x in spisok)
    spisok.sort(key=lambda x: x * max_len, reverse=True)
    return ''.join(spisok)
spisok = []
while True:
    element = input("Введите элемент списка(для завершения введите пустую строку):")
    if not element:
        break
    spisok.append(element)
print("Максимальное число: ", max_number(spisok))
