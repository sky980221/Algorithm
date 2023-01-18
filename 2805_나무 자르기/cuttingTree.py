import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, sum(trees)

while start <= end:
    treesum = 0
    mid = (start + end) // 2
    for i in trees:
        if i > mid:
            treesum += i - mid
    if treesum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
