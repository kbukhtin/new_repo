n = int(input())
mx = [[0] * n for i in range(n)]
_c, row, col, _flow = 1, 0, 0, 'right'

for i in range(1, n ** 2 + 1):
    mx[row][col] = i
    match _flow:
        case 'right':
            if col + 1 == n or mx[row][col + 1] != 0:
                _flow = 'down'
                row += 1
            else:
                col += 1
        case 'down':
            if row + 1 == n or mx[row + 1][col] != 0:
                _flow = 'left'
                col -= 1
            else:
                row += 1
        case 'left':
            if col - 1 == -1 or mx[row][col - 1] != 0:
                _flow = 'up'
                row -= 1
            else:
                col -= 1
        case 'up':
            if row - 1 == -1 or mx[row - 1][col] != 0:
                _flow = 'right'
                col += 1
            else:
                row -= 1

for i in range(n): print(*mx[i])
