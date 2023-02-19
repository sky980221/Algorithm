import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(permutations(arr, M))
arr.sort()
for i in range(len(arr)):
    print(*arr[i])

