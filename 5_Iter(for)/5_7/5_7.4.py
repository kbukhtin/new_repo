n, m = map(int, input().split())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m - 1, -1, -1):
        print(mx[i][j], end=' ')
    print()