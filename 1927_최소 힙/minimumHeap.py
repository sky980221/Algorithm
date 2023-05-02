import sys
import heapq
N = int(sys.stdin.readline())
heap = []
"""N개의 줄 동안 input 이 자연수면 배열에 추가, 0이라면 배열 min 값 출력하고 remove = pop 기능 사용, 배열 비어있는데 출력하라고 들어오면 0 출력"""

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print("0")
        else:
            result = heapq.heappop(heap)
            print(result)
    elif num > 0:
        heapq.heappush(heap,num)

