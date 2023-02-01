import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(int(ninput()))
start, end = min(arr), max(arr) * M
result = end
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in range(N):
        total += mid // arr[i]
    if total >= M:
        # 시간을 더 늘려줌
        end = mid - 1
        result = mid
    else:
        # 시간이 충분하다는거니까 시간을 줄여준다.
        start = mid + 1

answer = M
for i in range(M):
    answer += (result - 1) // arr[i]
for i in range(M):
    if result % arr[i] == 0:
        answer += 1
    if answer == N:
        print(i + 1)
        break
"""
Test Case 1
2 6
7
10

출력 
28
"""
