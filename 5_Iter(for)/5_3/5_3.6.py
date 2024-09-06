n, a = list(map(int, input().split())), int(input())

for i in range(len(n)):
    if n[i] == a:
        print(i + 1)
        break
else:
    print("ErrorValue")