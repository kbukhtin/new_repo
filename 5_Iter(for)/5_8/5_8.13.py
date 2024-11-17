mx = []
n = 8
_cord_f = []

for i in range(n):
    mx.append(list(input()))
    if 'F' in mx[i]:
        _cord_f.extend((i, mx[i].index('F')))

for j in range(n):
    for k in range(n):
        if ((j == _cord_f[0] or k == _cord_f[1]) or (abs(j - _cord_f[0]) == abs(k - _cord_f[1]))) and mx[j][k] != 'F':
            mx[j][k] = '+'

[print(*mem, sep='') for mem in mx]