n = int(input())
_c = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    _c += 1

print(_c)
