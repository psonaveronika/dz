s = input()
x, y = s.count(')'), s.count ('(')
if x > y:
    print('Не хватает', x - y, 'Закрывающей(их) скобки(ок)!')
elif x < y:
    print('Не хватает', y - x, 'Закрывающей(их) скобки(ок)!')    
else:
    print('Всё корректно!')