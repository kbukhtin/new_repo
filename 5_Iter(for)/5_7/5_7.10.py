n, m = map(int, input().split())
mx = []
result, point = 0, [0, 0]

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if mx[i][j] > result:
            result = mx[i][j]
            point[0], point[1] = i, j

print(result)
print(*point)
