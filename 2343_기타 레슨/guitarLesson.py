import sys
input = sys.stdin.readline
N, M = map(int, input().split())
video = list(map(int, input().split()))
videoMax = max(video)
start, end = videoMax, sum(video)
result = 10 ** 9
while start <= end:
    temp = 0
    count = 1
    mid = (start + end) // 2 
    for i in range(N):
        if temp + video[i] <= mid:
            temp = temp + video[i]

        else: 
            count += 1 
            temp = video[i]
        if count > M:
            break
    if count > M:
        start = mid + 1 
    else: 
        end = mid -1 
        if end  >= videoMax :
            result = min(result, mid) 

print(result)