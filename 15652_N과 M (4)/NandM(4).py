import sys
from itertools import combinations_with_replacement

# combinations_with_replacements 라는 라이브러리는 중복 조합(nHr)을 나타낸다.
N, M = list(map(int, sys.stdin.readline().split()))

arr = [(i + 1) for i in range(N)]
answer = list(combinations_with_replacement(arr, M))

for i in range(len(answer)):
    print(*(answer[i]))


"""
백트래킹 사용
n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1) 
"""