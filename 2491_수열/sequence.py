import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dpDec, dpInc = [1]*N, [1]*N

for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dpDec[i] = max(dpDec[i], dpDec[i-1]+1)
    if arr[i] >= arr[i-1]:
        dpInc[i] = max(dpInc[i], dpInc[i-1]+1)
print(max(max(dpDec), max(dpInc)))