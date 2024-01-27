import sys
input = sys.stdin.readline
N, M =  map(int, input().split())
cnt = 0
S = []
for _ in range(N):
    S.append(input())

for i in range(M):
    C = input()
    if C in S:
        cnt += 1

print(cnt)