spisok = []
while True:
    element = input("Введите элемент списка(для завершения введите пустую строку):")
    if element == "":
        break
    spisok.append(element)
def max_number(spisok):
    max_len = max(len(x) for x in spisok)
    spisok.sort(key=lambda x: x * max_len, reverse=True)
    return int(''.join(spisok))
print("Максимальное число: ", max_number(spisok))
