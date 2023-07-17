import sys

input = sys.stdin.readline


def dfs(v):
    for i in range(n):
        if check[i] == 0 and graph[v][i] == 1:
            check[i] = 1
            dfs(i)


n = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    check = [0 for _ in range(n)]
    dfs(x)
    print(*check)
