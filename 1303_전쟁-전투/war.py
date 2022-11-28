import sys 
from collections import deque
N, M = map(int, sys.stdin.readline().split())

soldiers = [list(sys.stdin.readline().strip()) for i in range(M)]
w, b = 0 , 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,team):
    queue = deque()
    queue.append((x,y))
    count = 0
    soldiers[x][y] == 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if soldiers[nx][ny] != 0 and soldiers[nx][ny] == team:
                queue.append((nx,ny))
                soldiers[nx][ny] = 0
                count += 1
    return (1 if count==0 else count)

for i in range(N):
    for j in range(M):
        if soldiers[i][j] != 0:
            if soldiers[i][j] == 'W':
                w += bfs(i,j,soldiers[i][j])**2
            else:
                b += bfs(i,j,soldiers[i][j])**2
print(w,b)