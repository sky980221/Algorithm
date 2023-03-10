import sys

N = int(sys.stdin.readline())
arr = []
dp = [0] * N
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

if len(arr) <= 2:
    print(arr)
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

    for i in range(2, N):
        dp[i] = max(dp[i - 3] + arr[i - 1], dp[i - 2] + arr[i])
    print(dp[-1])
"""

1개 또는 2개 
연속 3개 불가
마지막 무조건 밟아야 함 

case 1 
6
10
20
15
25
10
20

출력
75
"""
