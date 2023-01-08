import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')
"""
Test Case1
5
2 4 -10 4 -9
출력 
2 3 0 3 1
"""                                                                         