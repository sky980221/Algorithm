import sys

n, k = map(int, sys.stdin.readline().split())
arr = [(0, 0)]
chart = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    arr.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            chart[i][j] = chart[i - 1][j]
        else:
            chart[i][j] = max(chart[i - 1][j], v + chart[i - 1][j - w])

print(chart[n][k])