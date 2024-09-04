n = int(input())
k = n
_c = 0
while k != 1:
    if n % k == 0:
        _c = k
    k -= 1

print(_c)