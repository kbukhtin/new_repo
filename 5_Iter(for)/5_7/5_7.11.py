n, m = map(int, input().split())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

sportik, score = 0, [max(mx[0]), sum(mx[0])]

for i in range(n):
    s = 0
    ms = 0
    for j in range(m):
        s += mx[i][j]
        if mx[i][j] > ms:
            ms = mx[i][j]

    if ms > score[0]:
        sportik, score[0], score[1] = i, ms, s

    elif ms == score[0]:
        if s > score[1]:
            sportik, score[0], score[1] = i, ms, s

print(sportik)

