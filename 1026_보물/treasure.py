N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = 0
A.sort()
B.sort(reverse=True)

for i in range(N):
    C = C + A[i] * B[i]

print(C)