"""
n = int(input())

dp = [0]*(n+1)


if n == 3:
    print(n)

else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1]+dy[i-2]

    print(dp[n]%10007)

    """

n = int(input())

#1001이 아니라 n+1일 경우엔 dp[2]=2를 넣을 공간이 없음.
dp = [0]*1001
dp[1] = 1
dp[2] = 2

for i in range(2, n):
    dp[i+1] = dp[i] + dp[i-1]

print(dp[n] % 10007)