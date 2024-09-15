n, m = map(int, input().split())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    s = 0
    for j in range(m):
        s += mx[i][j]
    print(s, end=' ')
print()

for j in range(m):
    s = 0
    for i in range(n):
        s += mx[i][j]
    print(s, end=' ')