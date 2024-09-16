n = int(input())
mx = []
m = 0

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n -1, -1, -1):
        if i + j == n - 1 and mx[i][j] > m:
            m = mx[i][j]

print(m)