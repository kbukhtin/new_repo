n = int(input())
_t = tuple([x for x in range(n, n ** 2 + 1) if x % 2 != 0])
print(_t)