import sys
N,W,L = map(int,sys.stdin.readline().split())
Ai = list(map(int,sys.stdin.readline().split()))
bridge = [0] * W
time = 0

while bridge:
    time += 1
    bridge.pop(0)

    if Ai:
        if sum(bridge) + Ai[0] > L:
            bridge.append(0)
        else:
            bridge.append(Ai.pop(0))

print(time)
