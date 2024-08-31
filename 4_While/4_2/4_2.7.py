n, nl = int(input()), list(map(int, input().split()))
m, ml = int(input()), list(map(int, input().split()))

nl.sort(), ml.sort()

a = 0
b = 0
_c = 0

while a <= len(nl) - 1 and b <= len(ml) - 1:
    if nl[a] == ml[b] or nl[a] == ml[b] - 1 or nl[a] == ml[b] + 1:
        a += 1
        b += 1
        _c += 1
    else:
        if nl[a] > ml[b]:
            b += 1
        else:
            a += 1

print(_c)
