n = int(input())
x = map(int, input().split())
c = [0] * 201

for i in x:
    c[i + 100] += 1

for j in range(len(c)):
    if c[j] != 0:
        print((str(j - 100) + " ") * c[j], end="")
