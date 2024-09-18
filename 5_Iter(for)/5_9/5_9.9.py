from string import ascii_uppercase

n = int(input())

x = [ascii_uppercase[i] * (i+1) for i in range(n)]
print(x)
