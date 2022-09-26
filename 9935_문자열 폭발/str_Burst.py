import sys
input = sys.stdin.readline
 
S = list(input().rstrip())
burst = list(input().rstrip())
 
stack = []
 
for i in range(len(S)):
    stack.append(S[i])
    if stack[-1] == burst[-1] and len(stack) >= len(burst):
        if stack[-len(burst):] == burst:
            for i in range(len(burst)):
                stack.pop()
 
if stack:
    print("".join(stack))
else:
    print("FRULA")