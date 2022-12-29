"""
if 배열이 null인데 0이 입력되면 print 0
if 0이 입력되면 절댓값 가장 작은거 출력, 여러개면 그 중에서 가장 min 값 출력하고 제거 (pop)
if 0이 아닌 값이 입력 되면 배열에 추가 
"""
import sys
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
