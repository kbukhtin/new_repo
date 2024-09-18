a, b = map(int, input().split())

if a <= b:
    x = [i ** 2 for i in range(a, b + 1)]
else:
    x = [i ** 3 for i in range(a, b - 1, -1)]

print(x)
