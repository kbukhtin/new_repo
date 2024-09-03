a, b = map(int, input().split())

while a > 0:
    a, b = b % a, a

print(b)
