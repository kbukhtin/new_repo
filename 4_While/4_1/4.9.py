a, b = map(int, input().split())

_last_a = 0
_h = 0

while a:
    _h += 1
    a -= 1
    _last_a += 1
    if _last_a % b == 0:
        a += 1
        _last_a = 0

print(_h)