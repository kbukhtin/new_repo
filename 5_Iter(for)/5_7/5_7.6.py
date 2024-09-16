mx = []
for i in range(5):
    mx.append(list(map(int,input().split())))
x = y = 0

_findxyz = False
for i in range(5):
    for j in range(5):
        if mx[i][j] == 1:
            x = i
            y = j
            _findxyz = True
            break
    if _findxyz:
        break

print(abs(x - 2) + abs(y - 2))