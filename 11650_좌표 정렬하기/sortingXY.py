import sys
input = sys.stdin.readline

n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda i: (i[0], i[1]))		# lambda(람다)함수

for x, y in dots:
    print(x, y)