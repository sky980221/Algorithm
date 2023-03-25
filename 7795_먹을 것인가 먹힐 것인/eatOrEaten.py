import bisect
import sys
from bisect import bisect_left, bisect_right

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()

    A_pointer, B_pointer = 0,0
    while A_pointer < N and B_pointer < M:
        if A[A_pointer] > B[B_pointer]:
            cnt += 1
            B_pointer += 1
            if B_pointer == M:
                A_pointer += 1
                B_pointer = 0
        else: #소팅을 했기 때문에 A[A_pointer]와 B[B_pointer]가 같아 지는 순간 더이상 B를 탐색 할 필요 없이 A_pointer를 하나 올려주면 됨
            A_pointer += 1
            B_pointer = 0
    print(cnt)

"""
for i in range(A):
    for j in range(B):
        if i>=j:
        cnt++
        
bisect 사용법 
for i in A:
    cnt += bisect.bisect_left(B,i)
    


"""
