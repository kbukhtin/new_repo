x, y = map(int, input().split())

_c = 1

while x <= y:
    x += x * 0.15
    _c += 1

print(_c)