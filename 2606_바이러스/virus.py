"""
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

"""

# 20230711 복습

import sys

input = sys.stdin.readline
from collections import deque

numOfCom = int(input())  # 노드 개수
numOfPairs = int(input())  # 간선 개수
graph = [[] for _ in range(numOfCom+1)]
visited = [0] * numOfCom+1
for i in range(numOfPairs):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt +=1

dfs(1)
print(cnt)

def dfs():