a = list(map(int, input().split()))
b = True
for i in range(len(a) - 1):
    if a[i + 1] < a[i]:
        b = False
        break
print(b)
