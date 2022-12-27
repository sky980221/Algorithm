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
    i = 0
    j = len(arr)-1
    r = inf
    while i < j:
        tmp = arr[i]+arr[j]
        if tmp == 0:
            return arr[i], arr[j]
        if abs(tmp) < r:
            result = (arr[i], arr[j])
            r = abs(tmp)
        if tmp > 0:
            j -= 1
        else:
            i += 1
    return result
result = binary_search(arr)
print(result[0], result[1])