from collections import Counter

def f(text):
    u = max(text, key=len)
    c = Counter(text).most_common(1)[0][0]
    return 'Самое длинное:' + u + 'Самое частое:' + c


text = input().split()
print(f(text))
