n, m = map(int, input().split())
mx = []
for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n -1, -1, -1):
    for j in range(m):
        print(mx[i][j], end=' ')
    print()