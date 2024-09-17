n, m = map(int, input().split())
st = 0
mx = [[0] * m for i in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            mx[i][j] = st
            st += 1
    else:
        for j in range(m - 1, -1, -1):
            mx[i][j] = st
            st += 1

for i in range(n): print(*mx[i])
