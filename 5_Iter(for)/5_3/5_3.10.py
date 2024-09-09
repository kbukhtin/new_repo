n = input()
chet = nechet = 0

for i in range(len(n)):
    if (i+1) % 2 == 0:
        chet += int(n[i])
    else:
        nechet += int(n[i])

if (chet - nechet) % 11 == 0:
    print("YES")
else:
    print("NO")