N = int(input())

array = list(map(int,input().split()))

array = list(set(array))
array.sort()
for i in array:
    print(i,end = ' ')
'''end = ' ' 는 개행 지우기 '''

