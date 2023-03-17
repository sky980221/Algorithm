import sys

N = int(sys.stdin.readline())

dp = [0] * N
dp[0] = 1
dp[1] = 1
for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N-1])
"""

N       1       2       3       4                   5
        1       10    101,100   1000 1010 1001      10000 10100 10010 10001    
dp[i]   1       1       2       3


"""
