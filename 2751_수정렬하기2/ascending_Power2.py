from heapq import merge
import sys

N = int(sys.stdin.readline())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))


# sort 함수를 사용하기에는 100만이라는 숫자가 너무 커서 merge sort를 사용해야함 nlogn의 속도를 가지고 있음

def sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    new_list = []
    i = 0
    j = 0

    while (i < len(left)) & (j < len(right)):
        if left[i] > right[j]:
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    while (j < len(right)):
        new_list.append(right[j])
        j += 1
    while (i < len(left)):
        new_list.append(left[i])
        i += 1
    return new_list


for i in sort(array):
    print(i)