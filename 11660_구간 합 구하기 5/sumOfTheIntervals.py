import sys

N, M = map(int, sys.stdin.readline().split())
arrN = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (N + 1) for i in range(N + 1)]
# dp는 누적 합이라고 보면 된다.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arrN[i - 1][j - 1]
# 일차원일때 S[i] = S[i-1]+A[i]인 것과 같은 원리이다. 2차원 배열
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
