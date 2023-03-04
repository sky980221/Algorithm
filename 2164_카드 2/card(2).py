import sys
from collections import deque

N = int(sys.stdin.readline())

cards = [i + 1 for i in range(N)]
cards = deque(cards)
while len(cards) > 1:
    cards.popleft()
    if len(cards) > 1:
        cards.append(cards.popleft())
    else:
        break

print(*cards)
