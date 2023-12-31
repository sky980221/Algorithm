"""import sys
Arr1 = []
Arr2 = []
N = int(input())
# Arr1 = input().split()
Arr1.extend(list(map(int, input().split())))  # 입력 값을 리스트로 저장
M = int(input())
Arr2.extend(list(map(int, input().split())))  # 입력 값을 리스트로 저장
"""

"""
import sys

cnt = 0
# 쉽게 가자 쉽게
N = int(input())
Arr1 = [int(x) for x in input().split()]  # 입력 값을 리스트로 저장
M = int(input())
Arr2 = [int(x) for x in input().split()]  # 입력 값을 리스트로 저장

for num in Arr2:
    for num2 in Arr1:
        if num == num2:
            cnt += 1

    print(cnt, end=" ")
    cnt = 0
"""

import sys

input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result is None:
        print(0, end=" ")
    else:
        print(result, end=" ")
