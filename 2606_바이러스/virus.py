import sys
from collections import deque

n = int(sys.stdin.readline())  # 노드 개수
v = int(sys.stdin.readline())  # 간선 개수
graph = [[] for i in range(n + 1)]  # 그래프 초기화
visited = [0] * (n + 1)  # 방문한 컴퓨터인지 표시
for i in range(v):  # 그래프
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
visited[1] = 1  # 방문 표시
queue = deque([1])
while queue:
    c = queue.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            queue.append(nx)
            visited[nx] = 1
print(sum(visited) - 1)
