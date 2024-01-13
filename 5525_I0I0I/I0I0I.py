import sys
input = sys.stdin.readline
"""
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
P1 = IOI 니까 
PN = 
"""

N = int(input())
M = int(input())
S = input().rstrip()
PN = str("IO" * N + "I")
cnt = 0

for start in [i for i in range(M - len(PN) + 1) if S[i] == 'I']:
    end = start + len(PN)
    if S[start:end] == PN:
        cnt += 1
print(cnt)
