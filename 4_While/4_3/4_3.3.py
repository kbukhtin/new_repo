x = int(input())
_c = 1

while x:
    _c *= x % 10
    x //= 10

print(_c)
