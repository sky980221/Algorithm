import sys
N = int(input())
T = list(map(int,sys.stdin.readline().split()))
answer = [0] * N
stack = []


for i in range(N):
    tower = T[i]
    while stack and T[stack[-1]]< tower:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)
print(" ".join(map(str, answer)))