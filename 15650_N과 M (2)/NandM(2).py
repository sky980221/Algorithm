import sys
from itertools import combinations

N, M = list(map(int, sys.stdin.readline().split()))

# backtracking을 사용하라고 나와있긴함

arr = [i + 1 for i in range(N)]
answer = list(combinations(arr, M))
for i in range(len(answer)):
    print(*answer[i])

"""
def dfs(num):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    else:
        for i in range(num, n + 1):
            if not visited[i]:
                visited[i] = 1
                result.append(i)
                dfs(i + 1)
                visited[i] = 0
                result.pop()


n, m = map(int, input().split())
visited = [0] * (n + 1)
result = []
dfs(1)  
"""