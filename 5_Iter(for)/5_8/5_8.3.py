n = int(input())
mx = []
for i in range(n):
    mx.append(list(map(int, input().split())))

_count = 0
for i in range(n):
    for j in range(n):
        if mx[i][0] == mx[j][1]:
            _count += 1

print(_count)
