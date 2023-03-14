import sys

N = int(sys.stdin.readline())
arr = [0]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

dp = [0]
dp.append(arr[1])
if N > 1:
    dp.append((arr[1] + arr[2]))

for i in range(3, N + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]))
print((dp[N]))
