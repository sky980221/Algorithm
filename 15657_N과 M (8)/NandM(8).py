import sys
from itertools import combinations_with_replacement

# combinations_with_replacements 라는 라이브러리는 중복 조합(nHr)을 나타낸다.
N, M = list(map(int, sys.stdin.readline().split()))

arr = list(map(int , sys.stdin.readline().split()))
answer = list(combinations_with_replacement(arr, M))
answer.sort()
for i in range(len(answer)):
    print(*(answer[i]))
