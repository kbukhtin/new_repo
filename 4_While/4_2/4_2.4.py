n, k = map(int, input().split())

_c = 0
_z_time = 0
while n:
    if _z_time + (_c + 1) * 5 > 240 - k:
        break
    _c += 1
    _z_time += _c * 5
    n -= 1

print(_c)