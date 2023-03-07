import sys
from itertools import combinations_with_replacement
N,M = list(map(int, sys.stdin.readline().split()))
arr = set(map(int, sys.stdin.readline().split()))
arr = sorted(list(arr))
arr = list(combinations_with_replacement(arr, M))
for i in range(len(arr)):
    print(*(arr[i]))
