n = list(map(int, input().split()))
_d = {}
_d_1 = {}
_d[n[-2]] = n[-1]
n = n[:-2]

while len(n) != 0:
    _d_1[n.pop()] = _d
    _d_1, _d = _d.copy(), _d_1.copy()
    _d_1.clear()

print(_d)

# nums = list(map(int, input().split()))
#
# d = dict.fromkeys([nums.pop(-2)],nums.pop())
# while len(nums) > 0:
#         d = d.fromkeys([nums.pop(-1)],d)
#
# print(d)