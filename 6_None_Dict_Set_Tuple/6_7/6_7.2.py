a = input()
_d = {}

for i in a.lower():
    if i.isalpha():
        _d[i] = _d.get(i, 0) + 1

print(_d)