n = int(input())
i = 1
_c = []

while i * i <= n:
    if n % i == 0:
        _c.append(i)
        if i != n // i:
            _c.append(n // i)
    i += 1

print(sum(_c))