spisok = []
while True:
    element = input("Введите элемент списка(для завершения введите пустую строку):")
    if not element:
        break
    spisok.append(element)
print("Итоговый список: ", spisok)
