n, m = map(int, input().split())
mx_old = []
mx_new = []
count = 0

for i in range(n):
    mx_old.append(list(input()))

trash = input()

for i in range(n):
    mx_new.append(list(input()))

for i in range(n):
    for j in range(m):
        if mx_new[i][j] == mx_old[i][j]:
            count += 1

print(count)
