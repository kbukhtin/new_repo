a = input()
_s = 0
_count = 0

for i in a:
    if i.isdigit():
        _s += int(i)
        _count += 1

print(_count, _s)