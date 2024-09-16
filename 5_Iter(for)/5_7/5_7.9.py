n, m = map(int, input().split())
mx = []
sportik = result = 0

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    s = 0
    for j in range(m):
        s += mx[i][j]
    if s > result:
        result = s
        sportik = i

print(result, sportik, sep='\n')