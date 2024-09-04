n = int(input())
m_r = 0
f_r = 0

for i in range(n):
    m, f = map(int, input().split())
    if m > f:
        m_r += 1
    elif m < f:
        f_r += 1

if m_r > f_r:
    print("Mishka")
elif m_r < f_r:
    print("Chris")
else:
    print("Friendship is magic!^^")