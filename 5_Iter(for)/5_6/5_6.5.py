n, m = map(int, input().split())
_c = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i ** 2 + j == n and i + j ** 2 == m:
            _c += 1

print(_c)
