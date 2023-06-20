import sys


def trim(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]

n = int(sys.stdin.readline())
if n == 0 : print(0)
else :
    nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
    temp = trim(n * 0.15)
    if temp > 0 : nums = nums[temp : -temp]
    print(trim( sum(nums) / (n - temp*2) ))