a = input().split()
kek = []

for i in a:
    if i.lower() not in map(str.lower, kek):
        kek.append(i)

print(*kek)