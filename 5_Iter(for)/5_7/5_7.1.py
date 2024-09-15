n = int(input())
x = []

for i in range(n):
    x.append(list(map(int, input().split())))

s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s += x[i][j]

print(s)