import sys
from math import inf
input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))
def binary_search(A):
    start = 0
    end = len(A)-1
    r = inf
    while start < end:
        tmp = A[start]+A[end]
        if tmp == 0:
            return A[start], A[end]
        if abs(tmp) < r:
            result = (A[start], A[end])
            r = abs(tmp)
        if tmp > 0:
            end -= 1
        else:
            start += 1
    return result
result = binary_search(A)
print(result[0], result[1])