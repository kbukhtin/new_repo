n, x = map(int, input().split())
count = 0

for i in range(n):
    for j in range(n):
        if (i + 1) * (j + 1) == x:
            count += 1

print(count)