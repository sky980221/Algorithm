import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs(start):
    cnt = 1
    queue = deque([start])
    visit = [False for _ in range(n+1)]
    visit[start] = True

    while queue:
        current = queue.popleft()

        for nextcurrent in graph[current]:
            if not visit[nextcurrent]:
                visit[nextcurrent] = True
                cnt += 1
                queue.append(nextcurrent)
    
    return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

maxCnt = 1 
result = []

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt =cnt
        result.clear()
        result.append(i)
    elif cnt == maxCnt:
        result.append(i)

print(*result)