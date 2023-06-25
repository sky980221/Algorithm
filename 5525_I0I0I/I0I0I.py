import sys
import re

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

cnt = 0
pattern = 0
i = 1

while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            cnt += 1
        i += 1
    else:
        pattern = 0
    i += 1
print(cnt)