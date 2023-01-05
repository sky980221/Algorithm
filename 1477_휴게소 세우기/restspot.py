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
0 ≤ N ≤ 50
1 ≤ M ≤ 100
100 ≤ L ≤ 1,000
1 ≤ 휴게소의 위치 ≤ L-1
N+M < L
모든 휴게소의 위치는 중복되지 않음
입력으로 주어지는 모든 수는 정수

Test case 1
3 1 1000
300 701 800
출력 
300
"""
