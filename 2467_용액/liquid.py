import sys
from math import inf
N = int(sys.stdin.readline())
liquidArray = list(map(int, sys.stdin.readline().split()))
def binary_search(liquidArray):
    start = 0   
    end = N-1
    r = inf
    while start < end:
        mid = liquidArray[start]+liquidArray[end]
        if mid == 0:
            return liquidArray[start], liquidArray[end]
        if abs(mid) < r:
            result = (liquidArray[start], liquidArray[end])
            r = abs(mid)
        if mid > 0:
            end -= 1
        else:
            start += 1
    return result
result = binary_search(liquidArray)
print(*result)