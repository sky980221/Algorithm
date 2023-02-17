import sys
from itertools import combinations

N, M = list(map(int, sys.stdin.readline().split()))

# backtracking을 사용하라고 나와있긴함

arr = [i + 1 for i in range(N)]
answer = list(combinations(arr, M))
for i in range(len(answer)):
    print(*answer[i])
