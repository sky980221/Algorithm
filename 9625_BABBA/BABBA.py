import sys

input = sys.stdin.readline

n = int(input())
a = [1]
b = [0]

for i in range(n):
    a.append(b[i])
    b.append(b[i] + a[i])

print(a[-1], end=' ')
print(b[-1])
