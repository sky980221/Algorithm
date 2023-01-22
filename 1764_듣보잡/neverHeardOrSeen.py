import sys
N,M = list(map(int, sys.stdin.readline().split()))
heardArr = []
seenArr = []
commonArr = []
for _ in range(N):
    heardArr.append(sys.stdin.readline().rstrip())
for _ in range(M):
    seenArr.append(sys.stdin.readline().rstrip())

for i in heardArr:
    if i in seenArr:
        commonArr.append(i)
commonArr.sort()
print(len(commonArr))

for i in range(len(commonArr)):
    print(commonArr[i])
