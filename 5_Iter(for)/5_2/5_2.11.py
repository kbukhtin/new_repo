n = int(input())
x = "рок"

for i in range(n):
    y = input().lower()
    if x in y:
        print(i + 1, y.index(x) + 1)