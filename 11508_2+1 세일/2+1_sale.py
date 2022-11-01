N = int(input())
array=[]
for i in range(N):
    array.append(int(input()))
array.sort(reverse=True)

cost = 0
for i in range(N):
    if(i%3!=2):
        cost += array[i]
print(cost)