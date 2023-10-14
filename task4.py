from collections import Counter
def b(a):
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans

els = b(input())
print('Элемент | Частота')
ans = Counter(els)
print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')
