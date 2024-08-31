x = int(input())

while (y := int(str(x)[0])) != 1 and x <= 1000000000:
    x *= y


print(x)