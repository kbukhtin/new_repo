n, m = map(int, input().split())

_c = 0
_d = 0
while n:
    _c += 1
    _d += 1
    n -= 1
    if _c == m:
        n += 1
        _c = 0

print(_d)