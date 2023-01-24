import sys
L, K, C = list(map(int, sys.stdin.readline().split()))
arr = [0, *sorted([*map(int, input().split())]), L]
start, end = 1, L

count = 0
print(L,K,C)
print(arr)


"""
Test Case 1 
9 2 1
4 5

출력 
5 4 

통나무 길이는 L 
K개의 위치 
자르는 최대 횟수 C
"""
