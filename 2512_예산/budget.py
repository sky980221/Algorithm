import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in arr:
        if i >= mid:
            num+= mid
        else:
            num += i
    if num <= budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
