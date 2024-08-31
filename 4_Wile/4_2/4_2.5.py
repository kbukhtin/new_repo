n = int(input())
h = 0
_c = 0


while True:
    _c += 1
    h += _c
    n = n - h
    if n == 0:
        print(_c)
        break
    elif n < 0:
        print(_c - 1)
        break
