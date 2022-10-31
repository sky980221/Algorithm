x, y = map(int, input().split())
array = list(map(int,input().split()))
answer = []
for i in range(x-1):
    array[i+1] = array[i] + array[i+1]
array = [0] + array

for _ in range(y):
    a,b = map(int,input().split())
    answer.append(array[b] - array[a-1])

for i in range(y):
    print(answer[i])