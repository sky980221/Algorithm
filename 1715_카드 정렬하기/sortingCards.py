import sys
import heapq

N = int(sys.stdin.readline())
heapA = []
answer = 0
for _ in range(N):
    heapq.heappush(heapA, int(sys.stdin.readline()))

if len(heapA) == 1:
    print(0)
else:
    while len(heapA) > 1:
        firstCard = heapq.heappop(heapA)
        secondCard = heapq.heappop(heapA)
        answer += firstCard + secondCard
        heapq.heappush(heapA, firstCard + secondCard)
    print(answer)
