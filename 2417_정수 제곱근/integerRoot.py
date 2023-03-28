import sys
N = int(sys.stdin.readline())

start, end = 0, N

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 < N:
        start = mid + 1
    else:
        end = mid - 1

print(start)
