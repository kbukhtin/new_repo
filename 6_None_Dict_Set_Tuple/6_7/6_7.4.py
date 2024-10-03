s1, s2 = input(), input()

_d_s1 = {}
_d_s2 = {}

for i in s1:
    _d_s1[i] = _d_s1.get(i, 0) + 1

for i in s2:
    _d_s2[i] = _d_s2.get(i, 0) + 1

if _d_s1 == _d_s2:
    print("YES")
else:
    print("NO")