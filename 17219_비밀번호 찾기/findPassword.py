# 20231230 다시 풀기
import sys

# 입력 받기
N, M = map(int, input().split())
Arr1 = {}
for _ in range(N):
    a, b = input().split()
    Arr1[a] = b

Arr2 = [input().strip() for _ in range(M)]

# 결과 출력
for word in Arr2:
    if word in Arr1:
        print(Arr1[word])


"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for _ in range(N):
    site, ps = input().split()
    add[site] = ps

for _ in range(M):
    print(add[input().rstrip()])
    
"""