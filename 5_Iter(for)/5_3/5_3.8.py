a = input().lower()
_c = 0

for i in a:
    kol = a.count(i)
    if kol > _c:
        _c = kol

print(_c)