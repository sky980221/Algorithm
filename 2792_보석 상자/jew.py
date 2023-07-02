import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = []
for _ in range(M):
    colors.append(int(input()))

left = 1
right = max(colors)

while left <= right:
    mid = (left+right) // 2
    total = 0
    for color in colors:
        if color % mid == 0:
            total += color//mid
        else:
            total += (color//mid) + 1
    if total > N:
        left = mid + 1

    else:
        right = mid - 1

print(left)