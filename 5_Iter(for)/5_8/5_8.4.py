n, m = map(int, input().split())
mx = []
_c = 0

for i in range(n + 3):
    mx.append([0] * (m + 2))

for i in range(n):
    kek = list(input())
    for j in range(m):
        mx[i + 1][j + 1] = kek[j]

for i in range(n):
    for j in range(m):
        if mx[i+1][j+1] == '.':
            if mx[i][j + 1] != '*' and mx[i + 1][j] != '*' and mx[i + 1][j + 2] != '*' and mx[i + 2][j + 1] != '*':
                _c += 1

print(_c)