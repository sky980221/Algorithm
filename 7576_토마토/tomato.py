import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
graph= []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])
def BFS():   
    while queue:
        x,y = queue.popleft() 
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0<=nx< N and 0<= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])

BFS()


for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    count = max(count,max(i))

print(count-1)
"""
Test Case 1 
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
출력 -1 
"""