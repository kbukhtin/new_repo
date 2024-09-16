n = int(input())
mx = []

for i in range(n):
    mx.append(list(map(int, input().split())))

_isTrue = True
for i in range(n):
    for j in range(n):
        if i < j:
            if mx[i][j] != mx[j][i]:
                _isTrue = False
                break
    if _isTrue == False:
        break

if _isTrue:
    print('Yes')
else:
    print('No')