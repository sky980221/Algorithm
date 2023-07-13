from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
queue = deque([])
visit = [[False]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        if row[j] == 2:
            queue.append((i, j))
            visit[i][j] = True
            row[j] = 0
    board.append(row)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 1:
            queue.append((nx, ny))
            visit[nx][ny] = True
            board[nx][ny] = board[x][y] + 1

for row in board:
    for i in row:
        print(i, end=" ")
    print()