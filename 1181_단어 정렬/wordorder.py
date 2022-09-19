N = int(input())
array = []


for i in range (N):
    array.append(input())

array = list(set(array))
 
array.sort()
array.sort(key = len)

for i in array:
    print(i)
    