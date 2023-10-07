import random


def number():
    secret = random.randint(0, 100)
    while True:
        user_number = int(input("Введите число:"))
        if user_number > secret:
            print("Число меньше ")
        elif user_number < secret:
            print("Число больше")
        else:
            print("Вы угадали!")
            break


number()
