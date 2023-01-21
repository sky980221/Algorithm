import sys

A = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in arr:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[binary_search(i, 0, len(stack) - 1)] = i

print(len(stack) - 1)


"""
만약 이 전보다 작은게 나오면 포함 안 시키는 방식? 
이분 탐색을 이용해서 풀라는디 ...
"""
