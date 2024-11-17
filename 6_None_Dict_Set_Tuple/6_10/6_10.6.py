num = int(input()) + 1

while len(set(str(num))) != 4:
    num += 1
else:
    print(num)