n = list(map(int, input().split()))
a = None

for i in range(1, len(n)):
    if a == None and n[i] > 0:
        a = n[i]
    elif n[i] > 0 and n[i] < a:
        a = n[i]

if a != None:
    print(a)
else:
    print("Empty")