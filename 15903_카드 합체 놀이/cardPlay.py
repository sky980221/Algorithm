import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

cards = []
cardArr = [int(x) for x in sys.stdin.readline().split()]

for card in cardArr:
    heapq.heappush(cards, card)

for _ in range(m):
    firstCard = heapq.heappop(cards)
    secondCard = heapq.heappop(cards)

    heapq.heappush(cards, firstCard+secondCard)
    heapq.heappush(cards,firstCard+secondCard)

print(sum(cards))