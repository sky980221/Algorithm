from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
# 정점 개수, 간선 개수, 시작 노드
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs 방문기록
visited2 = [False] * (N + 1)  # bfs 방문기록


def bfs(V):
    queue = deque([V])
    visited2[V] = True  # 해당 V값을 방문 처리
    while queue:  # queue가 다 비면 종료
        V = queue.popleft()  # queue 맨 밑에 있는 값을 꺼낸 뒤에 출력
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited2[i] and graph[V][i]:
                queue.append(i)
                visited2[i] = True


def dfs(V):
    visited1[V] = True  # 첫번째 노드 방문
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:
            dfs(i)


dfs(V)
print()
bfs(V)