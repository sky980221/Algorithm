n = int(input())

dp = [0] * (n+1)
#d[1] == 1 이므로 연산이 필요하지 않음 
#d[2] == 1
#d[3] == 1
#d[4] == 2
#d[5] == 3
#d[6] == 1 + d[6//2] == 2 
#d[7] == 1 + d[6] == 3

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])