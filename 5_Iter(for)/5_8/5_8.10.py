n, m = map(int, input().split())
mx = [list(input()) for i in range(n)]

_sum, _row_score = 0, 0

for i in range(n):
    _c1 = 0
    for j in range(m):
        if mx[i][j] == 'S':
            break
        else:
            _c1 += 1
    else:
        _sum += _c1
        _row_score += 1

for j in range(m):
    _c2 = 0
    for i in range(n):
        if mx[i][j] == 'S':
            break
        else:
            _c2 += 1
    else:
        _sum += (_c2 - _row_score)

print(_sum)
