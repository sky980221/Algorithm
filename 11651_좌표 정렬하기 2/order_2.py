import sys
num = int(sys.stdin.readline())
a = []
for i in range(num):
    [x, y] = map(int, sys.stdin.readline().split())
    reverse = [y, x]
    a.append(reverse)
b = sorted(a)
for i in range(num):
    print(b[i][1], b[i][0])