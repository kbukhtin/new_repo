n = int(input())
_c_v = 0
_c_c = 0

while _c_v + (x := int(input())) <= n:
    _c_v += x
    _c_c += 1

print(f"Довольно!\n{_c_v}\n{_c_c}")