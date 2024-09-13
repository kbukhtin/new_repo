n = int(input())
_c = 0
for i in range(n + 1, 2 * n):
    hm = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            hm += 1
            break
    if hm == 0:
        _c += 1
print(_c)
