n, m = map(int, input().split())
mx = [list(input().split()) for i in range(n)]

_blackWhite = True

for i in range(n):
    for j in range(m):
        if mx[i][j] not in ('WGB'):
            _blackWhite = False
            break
    else:
        continue
    break

print("#Black&White" if _blackWhite else "#Color")