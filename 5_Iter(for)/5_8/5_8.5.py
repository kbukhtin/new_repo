n, m = map(int, input().split())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(1, m):
        mx[i][j] = mx[i -1][j] + mx[i][j-1]

for i in range(n):
    for j in range(m):
        print(mx[i][j], end=" ")
    print()