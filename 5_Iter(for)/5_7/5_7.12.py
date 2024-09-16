n, m = map(int, input().split())
mx = []
score = [0, 0]

for i in range(n):
    mx.append(list(map(int, input().split())))

for i in range(n):
    top = 0
    for j in range(m):
        if mx[i][j] > top:
            top = mx[i][j]

    if top > score[0]:
        score[0], score[1] = top, 1
    elif top == score[0]:
        score[1] += 1

print(score[1])