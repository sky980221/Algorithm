import sys

N, M = map(int, sys.stdin.readline().split())
heardArr = set()
seenArr = set()

for _ in range(N):
    heardArr.add(sys.stdin.readline().rstrip())
for _ in range(M):
    seenArr.add(sys.stdin.readline().rstrip())

commonArr = sorted(list(heardArr & seenArr))
print(len(commonArr))

for i in commonArr:
    print(i)

# 배열로 풀면 시간 초과가 떠서 안되고 set()을 이용해 교집합으로 풀어야함. 주의할 점은 set에 element를 추가할 때는 append가 아닌 add를 사용해준다.
