a = input()
n = 0

while n != len(a):
    x = a[n]
    if x == 'e' or x == 'a':
        print("Ага! Нашлась")
        break
    print(f"Текущая буква: {x}")
    n += 1
else:
    print("Распечатали все буквы")