N, T = map(int,input().split())
result = []
"""
이분 탐색을 사용하지 않는 코드
for i in range(N):
    si, li, ci = map(int,input().split())
    for j in range(ci):
        if si + li * j >= T:
            result.append( si + li * j - T) 
            break

if len(result) == 0:
    print("-1")
else:
    print(min(result))
"""
#이분 탐색을 이용한 코드 
for _ in range(N):
    si, li, ci = map(int, input().split())
    li = [si+li*i for i in range(ci)]
    if li[-1] < T:
        continue
    start, end = 0, ci-1
    a = 0
    while start <= end:
        mid = (start+end)//2
        if li[mid] >= T:
            a = mid
            end = mid-1
        else:
            start = mid+1
    result.append(li[a]-T)
print(min(result) if result else -1)