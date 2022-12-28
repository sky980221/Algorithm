import sys
import itertools
from math import inf
N = int(sys.stdin.readline())
liquidArray = list(map(int, sys.stdin.readline().split()))
 
"""
#두 개 용액 합쳐서 0에 가장 가깝게 만들어라 = 절댓값이 작아야함
answerArray = list(itertools.combinations(liquidArray,2))
newArray = []
for i in range(len(answerArray)):
    newArray.append(abs(sum(answerArray[i])))
answer = newArray.index(min(newArray))
print(*answerArray[answer])
"""
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