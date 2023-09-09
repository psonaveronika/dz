x = float(input())
y = float(input())
if x == 0:
    print('Точка лежит на оси ординат')
elif y == 0:
    print('Точка лежит на оси абсцисс')
elif x > 0 and y > 0:
    print('Точка лежит в первой четверти')
elif x < 0 and y > 0:
    print('Точка лежит в второй четверти')
elif x < 0 and y < 0:
    print('Точка лежит в третьей четверти')
elif x > 0 and y < 0:
    print('Точка лежит в четвёртой четверти')
else:
    print('Точка лежит в начале координат')
