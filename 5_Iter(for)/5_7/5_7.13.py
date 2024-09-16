mx = []
for i in range(4):
    mx.append(list(input()))

_isNotBf = False
for i in range(0, 3):
    for j in range(0, 3):
        if mx[i][j] == mx[i][j + 1] == mx[i + 1][j] == mx[i + 1][j + 1]:
            _isNotBf = True
            break
    if _isNotBf:
        print("No")
        break
else:
    print("Yes")
