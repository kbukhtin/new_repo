n, m = map(int, input().split())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        mx[i][j] = mx[i][j + 1] + mx[i + 1][j]

for i in range(n):
    for j in range(m):
        print(mx[i][j], end=' ')
    print()
