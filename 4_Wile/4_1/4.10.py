x = int(input())
y = 0
n = True
while n:
    z = pow(2, y)
    if z == x:
        print(y)
        n = False
    elif z > x:
        print("НЕТ")
        n = False
    y += 1
