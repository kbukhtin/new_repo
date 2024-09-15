n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for j in range(n):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()

