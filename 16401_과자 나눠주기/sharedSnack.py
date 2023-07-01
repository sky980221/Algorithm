import sys
input = sys.stdin.readline
"""앞으로 이 두 줄로 해야겠당 """
m, n  = map(int,input().split())
L = list(map(int, input().split()))
start = 1
end = int(1e9)
answer = 0
while start <= end:
    mid = (start+end)//2
    c = 0
    for i in L:
        c += i//mid
    if c >=m:
        answer = max(answer,mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)