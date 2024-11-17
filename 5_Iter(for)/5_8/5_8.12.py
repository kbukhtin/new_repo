mx = []
_cord_s = []
n = 8

for i in range(n):
    mx.append(list(input()))
    if 'S' in mx[i]:
        _cord_s.extend((i, mx[i].index('S')))

for j in range(n):
    for k in range(n):
        if (abs(j - _cord_s[0]) == abs(k - _cord_s[1])) and mx[j][k] != 'S':
            mx[j][k] = '+'

[print(*k, sep='') for k in mx]
