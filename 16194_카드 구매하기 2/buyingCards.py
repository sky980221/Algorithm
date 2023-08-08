import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst = [0] + lst

dp = [999999999 for i in range(1001)]
dp[0] = 0

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = min(dp[i], lst[j] + dp[i - j])

print(dp[n])