mx = []
n = 8
_cord_h = []

for i in range(n):
    mx.append(list(input()))
    if 'H' in mx[i]:
        _cord_h.extend((i, mx[i].index('H')))

for j in range(n):
    for k in range(n):
        if abs(_cord_h[0] - j) * abs(_cord_h[1] - k) == 2:
            mx[j][k] = '+'

[print(*mem, sep='') for mem in mx]