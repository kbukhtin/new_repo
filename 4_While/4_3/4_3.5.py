x = int(input())
_c = 0

while x:
    if x % 10 == 7:
        _c += 1
    x //= 10

print(_c)
