import sys

S, C = map(int, sys.stdin.readline().split())
arrL = []
cnt = 0
left = 0
for _ in range(S):
    arrL.append(int(sys.stdin.readline()))
arrL.sort()
usingForChicken = 0
start, end = 0, 1000000000 #왜 min(arrL)이 아닌지 잘 모르겠음 ! 자르는 건 다 똑같을 것 같은데
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arrL:
        if mid == 0:
            mid = 1
        cnt += i // mid
    if cnt >= C:
        usingForChicken = max(usingForChicken, mid)
        start = mid + 1
    else:
        end = mid - 1
left = sum(arrL) - C * usingForChicken

print(left)
