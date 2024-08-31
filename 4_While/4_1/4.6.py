n = int(input())
k = 1

while (mem := pow(k, 2)) <= n:
    print(mem)
    k += 1
