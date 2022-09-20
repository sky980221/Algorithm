from heapq import merge
from turtle import left


N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
'''sort 함수를 사용하기에는 100만이라는 숫자가 너무 커서 merge sort를 사용해야함 nlogn의 속도를 가지고 있음 '''

def mergeSort(array):
    if len(array) <=1:
        return array
    mid = len(array)//2 
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    left1 = mergeSort(left)
    right1 = mergeSort(right)
    return = merge(left1, right1)

def merge(left, right):
    i=j=0
    sorted_list = []
    

while i < len(left) and j < len(mid):



for i in array:
    print(i)
