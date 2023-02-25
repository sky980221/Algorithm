import sys

N = int(sys.stdin.readline())
arr = []
newArr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

"""
하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

가장 적게 드는 놈 x 사용되는 로프 개수 = 최대 중량

10 15 20 25 

10 x 4 = 40 
15 x 3 = 45 
20 x 2 = 40
25 x 1 = 25
중에 max 구해서 print
"""

arr.sort()

for i in range(1 , len(arr)+1):
    newArr.append(arr[len(arr)-i]*i)
print(max(newArr))
