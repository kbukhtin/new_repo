a = input()
c = []

for i in a:
    if i == '(':
        c.append(i)
    elif len(c) != 0 and i == ')':
        c.pop()
    elif len(c) == 0 and i == ')':
        print("NO")
        break
else:
    if len(c) != 0:
        print("NO")
    else:
        print("YES")