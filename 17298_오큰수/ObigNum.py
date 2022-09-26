import sys
input = sys.stdin.readline

n = int(input())
Ai = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(Ai)):
    while stack and Ai[stack[-1]] < Ai[i]:
        answer[stack.pop()] = Ai[i]
    stack.append(i)
print(*answer)