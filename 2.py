from collection import Counter

text = input().split()
def f(text):
    u = max(text, key = len)
    c = Counter(text)
    a = max(c, key = lamda x: c[x])
    print ('Самое длинное: '+ u +',самое частое:' + a')
f(text)