def a(n):
    f = [0, 1, 1]
    if n > 3:
        for _ in range(n - 2):
            f.append(f[-2] + f[-1])
    return f[:n]    # При 2, 1 или 0


print(*a(int(input())), sep=' ')
