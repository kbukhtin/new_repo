n = int(input())
_c = []

for i in range(n):
    x = input()
    if "соль" not in x:
        _c.append(x)

print(", ".join(_c))