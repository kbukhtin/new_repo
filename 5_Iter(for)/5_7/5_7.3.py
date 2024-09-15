n = int(input())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

for j in range(n - 1, -1, -1):
    for i in range(n - 1, -1, -1):
        print(mx[i][j], end=' ')
    print()
