from collections import deque
import sys
N = int(sys.stdin.readline())
Ai = deque(map(int,sys.stdin.readline().split()))

clear = deque(range(1, N+1))
before = deque()

while Ai:
    t= Ai.pop()
    a= clear.popleft() 
    if t == 1:
        before.appendleft(a)
    elif t == 2:
        before.insert(1,a)
    elif t == 3:     
        before.append(a)
print(*before)