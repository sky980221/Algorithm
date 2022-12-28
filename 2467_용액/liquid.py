import sys
import itertools
from math import inf
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
 
"""
#두 개 용액 합쳐서 0에 가장 가깝게 만들어라 = 절댓값이 작아야함
answerArray = list(itertools.combinations(arr,2))
newArray = []
for i in range(len(answerArray)):
    newArray.append(abs(sum(answerArray[i])))
answer = newArray.index(min(newArray))
print(*answerArray[answer])
"""
def binary_search(arr):
    start = 0   
    end = N-1
    r = inf
    while start < end:
        tmp = arr[start]+arr[end]
        if tmp == 0:
            return arr[start], arr[end]
        if abs(tmp) < r:
            result = (arr[start], arr[end])
            r = abs(tmp)
        if tmp > 0:
            end -= 1
        else:
            start += 1
    return result
result = binary_search(arr)
print(result[0], result[1])