import sys
N,M,L = map(int,sys.stdin.readline().split())
arr = [0]+ list(map(int,sys.stdin.readline().split())) +[L]
arr.sort()

start, end = 1, L-1
result = 0
while start <= end:
    count = 0 
    mid = (start+end)//2
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1]>mid: 
            #두 휴게소 사이의 거리가 mid보다 클 시엔
            #그 거리 -1을 mid로 나눈 값을 카운트에 더한다 
            count += (arr[i]-arr[i-1] - 1)//mid
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)
"""
이분탐색
1. 입력을 받으면서 휴게소 배열(arr)의 양 끝에 출발지점과 도착지점을 추가해주고 정렬
2. start, end는 휴게소 위치의 범위
3. 이분탐색
    - mid : 가장 멀리 떨어져 있는 휴게소 사이 거리
    - count : 설치해야 할 휴게소 개수
    - 모든 거리를 완전 탐색을 해서 mid보다 큰 경우, 해당 mid로 나누어서 설치해야 할 휴게소 개수를 구한다.
    - 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다.
    - 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다. (조건 만족은 했으므로 result = mid)
4. result 출력
"""