n = int(input())
_sum = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        _sum += i

print(_sum)
