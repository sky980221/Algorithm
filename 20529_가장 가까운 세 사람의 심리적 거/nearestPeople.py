import sys

T = int(sys.stdin.readline())

while T:
    T = T-1
    N = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().split()))
    ans = 999999
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if arr[i][x] != arr[j][x]:
                            tmp = tmp + 1
                        if arr[j][x] != arr[k][x]:
                            tmp = tmp + 1
                        if arr[i][x] != arr[k][x]:
                            tmp = tmp + 1
                    ans = min(ans, tmp)
        print(ans)