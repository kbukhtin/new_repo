x = int(input())
_min = 9
_max = 0

while x:
    z = x % 10
    if z < _min:
        _min = z
    if z > _max:
        _max = z
    x //= 10

print(f'{_min}\n{_max}')
