import sys

N = int(sys.stdin.readline())
nArray = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mArray = list(map(int, sys.stdin.readline().split()))
nArray.sort()
status = False
for i in mArray:
    start, end = 0, len(nArray) - 1
    while start <= end:
        mid = (start + end) // 2
        if i < nArray[mid]:
            end = mid - 1
            status = False
        elif i > nArray[mid]:
            start = mid + 1
            status = False
        else:
            status = True
            break
    if not status:
        print("0")
    else:
        print("1")