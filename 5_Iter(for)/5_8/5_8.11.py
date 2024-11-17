mx = []
n = 8
kek = []
for i in range(n):
    mx.append(list(input()))
    if 'T' in mx[i]:
        kek.extend((i, mx[i].index('T')))

for j in range(n):
    for k in range(n):
        if (j == kek[0] or k == kek[1]) and mx[j][k] != 'T':
            mx[j][k] = '+'

for g in range(n):
    print(''.join(mx[g]))
