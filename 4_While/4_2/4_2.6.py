a, b = map(int, input().split())
_l1 = list(map(int, input().split()))
_l2 = list(map(int, input().split()))

c = []

while len(_l1) > 0 and len(_l2) > 0:
    if _l1[0] < _l2[0]:
        c.append(_l1.pop(0))
    else:
        c.append(_l2.pop(0))

if len(_l1) == 0 and len(_l2) != 0:
    c.extend(_l2)
elif len(_l1) != 0 and len(_l2) == 0:
    c.extend(_l1)

print(*c)
