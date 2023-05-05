import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        """IDEA: y = -x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다.
        그 결과 heappop을 사용하게 되면 힙에 있는 최댓값이 반환되는 것을 확인할 수 있다. 이때 실제 원소 값은 튜플의 두 번째 자리에 저장되어 있으므로 [1] 인덱싱을 통해 접근하면 된다. """
        heapq.heappush(heap, (-num, num))
    elif num == 0 and len(heap) > 0:
        print(heapq.heappop(heap)[1])
    elif num == 0 and len(heap) == 0:
        print("0")
""" 
x가 자연수면 배열에 x 추가
x가 0이면 배열에서 가장 큰 값 출력하고 제거
"""