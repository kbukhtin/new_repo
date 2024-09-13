n = int(input())
x = list(map(int, input().split()))
_c = 0

for i in range(n):
    for j in range(n - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
            _c += 1
print(*x)
print(_c)