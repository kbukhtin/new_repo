n = int(input())
_c = []
i = 1

while i * i <= n:
    if n % i == 0:
        _c.append(i)
        if i != n // i:
            _c.append(n // i)
    if len(_c) > 2:
        break
    i += 1

if len(_c) == 2:
    print("Yes")
else:
    print("No")