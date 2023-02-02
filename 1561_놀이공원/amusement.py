import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, 2000000000 * 30
time = 0
while start <= end:
    mid = (start + end) // 2
    total = M #맨 처음에는 다 타기 때문에 total = M
    result = 0
    for i in range(M):
        total += mid // arr[i]
    if total >= N:
        end = mid -1
        result = mid
    else:
        start = mid + 1
"""
3. 구한 시간 - 1분까지 몇 명의 아이를 태울 수 있는지 탐색합니다.

4. 구한 시간에 탑승하는 아이들을 계산하면서 제일 마지막에 탑승하는 놀이기구의 번호를 출력합니다. (놀이기구 탑승 인원이 N명이 될 때의 놀이기구 번호를 출력하면 됩니다)
"""
answer = M
for i in range(M):
    answer += (result-1) // arr[i]
for i in range(M):
    if result % arr[i] == 0:  # 최소 시간에 탑승한 아이
        answer += 1
    if answer == N: #마지막 친구가 왔다면 그 순간 몇 번째 놀이기구인지 print, i는 0부터 시작하기 때문에 +1 해줍니다.
        print(i + 1)
        break
"""
3 5
7 8 9 7 8

출력 
3
"""