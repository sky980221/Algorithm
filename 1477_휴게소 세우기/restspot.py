import sys
N,M,L = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))

arr.append(0)
arr.append(L-1)
arr.sort()
start, end = 0, arr[-1]



while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, len(arr)):
        if mid < arr[i]-arr[i-1]:
            cnt += (arr[i]-arr[i-1] - 1)//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)
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
