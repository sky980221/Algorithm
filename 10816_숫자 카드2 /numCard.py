import sys

N = int(input())
arr1 = sorted(list(map(int, input())))
M = int(input())
arr2 = sorted(list(map(int, input())))

cnt = {}
for i in arr1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
for i in arr2:
    if i in cnt:
        print(cnt[i], end='')
    else:
        print(0, end='')
