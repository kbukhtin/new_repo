a = list(map(int, input()))
c = [0] * 10

for i in a:
    c[i] += 1

for i in range(10):
    if c[i] != 0:
        print(i, c[i])