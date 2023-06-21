import sys

N, M, B = map(int, sys.stdin.readline().split())
array = []
solve = []
for i in range(N):
    array += (map(int, sys.stdin.readline().split()))
for i in range(min(array), max(array) + 1):
    bag = B
    sec = 0
    for ground in array:
        if (ground - i) > 0:
            bag += (ground - i)
            sec += 2 * (ground - i)
        elif (ground - i) < 0:
            bag += (ground - i)
            sec += 1 * (ground - i) * -1
    if bag >= 0:
        solve.append([sec, i])
solve.sort(key=lambda x: (x[0], -x[1]))
print(solve[0][0], solve[0][1])
