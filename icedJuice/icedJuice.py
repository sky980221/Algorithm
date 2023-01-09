import sys
N, M = map(int, sys.stdin.readline().split())
#가로는 M 세로는 N
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
def dfs(x,y):
    if x <0 or x >=N or y<0 or y>=M:
        return False 
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True    
    return False
result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result += 1 
print(result)

"""
4 5
00110
00011
11111
00000
"""