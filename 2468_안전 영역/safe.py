from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
height_list = [list(map(int, input().split())) for _ in range(N)]
min_val, max_val = min(map(min, height_list)), max(map(max, height_list))


def dfs(x, y, h, visited):
    q = deque([(x, y)])
    visited[y][x] = True
    while q:
        x, y = q.pop()

        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < N and -1 < ay < N and height_list[ay][ax] > h and not visited[ay][ax]:
                visited[ay][ax] = True
                q.append((ax, ay))


def search(h):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if height_list[i][j] > h and not visited[i][j]:
                dfs(j, i, h, visited)
                cnt += 1

    return cnt


def solve():
    answer = 1
    for i in range(min_val, max_val):
        answer = max(answer, search(i))

    print(answer)


solve()
