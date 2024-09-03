x = int(input())
_c = 0

while x:
    _c += x % 10
    x //= 10

print(_c)
