import sys 
N,C = list(map(int, sys.stdin.readline().split())) 
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
start, end = 1, arr[-1]-arr[0] 
#공유기 사이의 거리를 start : 최소거리 end : 최대거리로 놓는다.  
result = 0

while start <= end:
    count = 1
    #설치한 공유기의 개수 
    mid = (start+end)//2
    #공유기 사이의 거리
    routerSpot = arr[0]
    for i in range(1, len(arr)): 
        if  arr[i] >= routerSpot + mid:
#핵심 문장 : 목표지점이 시작점에서 mid만큼 더 한 것보다 멀거나 같으면 그 곳에 공유기를 설치하고 그곳부터 다시 출발한다. 
            count = count + 1
            routerSpot = arr[i] 
#이미 설치한 공유기의 개수가 목표 공유기 개수보다 많으면 공유기 사이 거리를 늘려 공유기 개수를 줄인다. 
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1 
print(result)

"""
Test case 1 
5 3
1
2
8
4
9

출력 
3
"""