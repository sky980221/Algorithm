import sys
from itertools import permutations
N, M = list(map(int, sys.stdin.readline().split()))
arr = sorted(list(map(int, sys.stdin.readline().split())))
arr = sorted(set(permutations(arr, M)))

for i in range(len(arr)):
    print(*(arr[i]))
