import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))

point1 = ((0 - x) ** 2 + (y - y) ** 2) ** (1 / 2)
point2 = ((x - x) ** 2 + (0 - y) ** 2) ** (1 / 2)
point3 = ((x - x) ** 2 + (h - y) ** 2) ** (1 / 2)
point4 = ((w - x) ** 2 + (y - y) ** 2) ** (1 / 2)

print(int(min(point1, point2, point3, point4)))
