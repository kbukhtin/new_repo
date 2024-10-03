n = int(input())
_d = {}

for i in range(n):
    name = input()
    if name not in _d:
        _d[name] = 1
        print('OK')
    else:
        print(f'{name}{_d[name]}')
        _d[name] += 1