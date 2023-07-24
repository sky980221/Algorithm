from collections import deque

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

q = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            q.append((i, j))

longest = 0
while q:
    x, y = q.popleft()
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx in range(n) and ny in range(m):
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                longest = maps[nx][ny]
                q.append((nx, ny))

print(longest - 1)
