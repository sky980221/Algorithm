from sys import stdin
from collections import deque

input = stdin.readline

"""
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    graph[y][x] = 0
    while que:
        a, b = que.pop()
        for i in range(8):
            ny = b + dy[i]
            nx = a + dx[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                que.append((nx, ny))
                graph[ny][nx] = 0


result = []
while True:
    res = 0
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(j, i)
                res += 1
    result.append(res)

for i in result:
    print(i)
    
    
"""
# 2회차 풀이 20230727

from collections import deque
import sys

input = sys.stdin.readline

d = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = True

    while q:
        r, c = q.popleft()

        for i in range(8):
            dr = r + d[i][0]
            dc = c + d[i][1]

            if 0 <= dr < h and 0 <= dc < w and maps[dr][dc] == 1 and not visited[dr][dc]:
                visited[dr][dc] = True
                q.append([dr, dc])


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
