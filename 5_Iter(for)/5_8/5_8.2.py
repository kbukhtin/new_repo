n = int(input())
a, b, c = map(int, input().split())
mx = []

for i in range(n):
    mx.append([0] * n)

for i in range(n):
    for j in range(n):
        if i < j: mx[i][j] = a
        elif i == j: mx[i][j] = c
        else: mx[i][j] = b


for i in range(n):
    print(*mx[i])
