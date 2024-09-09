a, b = input(), input().split()

for i in b:
    if a.lower() in i.lower():
        print(i)