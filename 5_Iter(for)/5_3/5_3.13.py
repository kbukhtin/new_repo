a = input()
c = []

for i in a:
    if i in "{[(":
        c.append(i)
    elif len(c) != 0 and i == "}" and c[-1] == "{" or len(c) != 0 and i == ")" and c[-1] == "(" or len(c) != 0 and i == "]" and c[-1] == "[":
        c.pop()
    elif len(c) == 0 and  i in "}])":
        print("NO")
        break
else:
    if len(c) != 0:
        print("NO")
    else:
        print("YES")