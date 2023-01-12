from collections import deque
N,M = map(int, input().split())
arr = [] 
for i in range(N):
    arr.append(list(map(int,input())))

check = [[0] * M for _ in range(N)]
count = [[0]* M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    #시작 위치를 큐에 삽입
    queue.append((0,0))
    check[0][0] = 1 
    count[0][0] = 1 
 
    #queue의 요소가 전부 사라질 떄까지 반복
    while queue:
        #큐의 최하단 요소를 현재 위치에 저장하고 큐에서 제거
        x, y = queue.popleft()
        #상하좌우 탐색
        for i in range(4):
            #다음 노드 위치 
            nx = x + dx[i]
            ny = y + dy[i]
        
            #다음 노드는 우선 미로 안에 있어야 하니까 0보다는 커야하고 가장 최외곽인 N,M 보다는 작아야합니다.
            if (nx >= 0 and nx < N and ny >= 0 and ny < M):
                #인접한 노드를 방문할 수 있는지 확인 
                if (check[nx][ny] == 0 and arr[nx][ny] == 1):
                    #방문할 수 있나? 그렇다면 큐에 삽입
                    queue.append((nx,ny))
                    #인접 노드 방문 기록
                    check[nx][ny] == 1
                    #직전 칸수  + 1 해줍니다
                    count[nx][ny] = count[x][y] + 1 
                
    #가장 오른쪽 아래까지의 최단거리 반환

    return count[N-1][M-1]

print(BFS())

"""
TestCase 1 
5 6
101010
111111
000001
111111
111111

출력 10
"""