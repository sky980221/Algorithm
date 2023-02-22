import sys

N = int(sys.stdin.readline())
fKg, tKg = 5, 3
tCount = 0

fCount = N//fKg
tmp = fCount * fKg
while 1:
    if N == 3:
        print(1)
        break
    if (fCount or tCount) <= 0:
        print(-1)
        break
    if tmp < N:
        tmp = tmp + tKg
        tCount += 1
    elif tmp == N:
        print(fCount+tCount)
        break
    elif tmp > N:
        tmp = tmp - fKg
        fCount -= 1

