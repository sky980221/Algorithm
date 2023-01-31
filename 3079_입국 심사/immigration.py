import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
start, end = min(arr), max(arr) * M
result = end
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in range(N):
        total += mid//arr[i]
    if total >= M:
        #시간을 더 늘려줌
        end = mid - 1
        result = min(result, mid)
    else:
        #시간이 충분하다는거니까 시간을 줄여준다.
        start = mid + 1

print(result)
"""
Test Case 1
2 6
7
10

출력 
28
"""
