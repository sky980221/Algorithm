import sys
from collections import deque

MAX = 100000
N, K = list(map(int, sys.stdin.readline().split()))
# 만약 원하는 결과가 아니라면 == 더이상 앞에 노드가 없는 경우
visited = [0] * MAX


def BFS(V):
    queue = deque([V])
    while queue:
        V = queue.popleft()
        if V == K:
            # 만약 목표에 도달했다면
            return visited[V]
        for i in (V - 1, V + 1, 2 * V):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[V] + 1
                print(visited[i])
                queue.append(i)


print(BFS(N))
