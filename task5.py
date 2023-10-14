def b(a):
    ans = []
    while a:
        ans.append(a)
        a = input()
    return ans


def sub(*args) -> float:
    return sum(args) / len(args)


print(sub(*map(int, b(input()))))
