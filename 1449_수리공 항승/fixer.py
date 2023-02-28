import sys

N, L = map(int, sys.stdin.readline().split())
fix = list(map(int, sys.stdin.readline().split()))
fix.sort()
count = 1
start = fix[0]
for i in fix:
    if i in range(start, start + L):
        continue
    else:
        start = i
        count += 1

print(count)

"""
4 2
1 2 100 101
"""
